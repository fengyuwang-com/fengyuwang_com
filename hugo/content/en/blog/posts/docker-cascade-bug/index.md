---
title: "I Filed Docker a Cascading Bug"
date: 2026-09-05
description: "A zero-byte file brought down the engine. Fix one, the next one appears."
slug: "docker-cascade-bug"
tags: ["Docker", "Debugging"]
draft: false
translationKey: "docker-cascade-bug"
---

Most people stop at "a reboot fixes it" when they file a bug. I couldn't stop there — I wanted to know which layer had rotted.

The symptom was simple: from version 4.71 on, Docker Desktop crashes on startup, in a loop, on Windows Insider Build 26200. Still unfixed as of 4.82.

I dug until I found the nail. The new inference manager creates an AF_UNIX socket file on NTFS, and Windows implements that kind of socket by hanging it on an NTFS reparse point. When Docker exits uncleanly — crash, force kill, power loss — the zero-byte file stays on disk carrying an unclaimed marker. On the next start the program tries to delete it, Windows answers error 1920, refused. The program reads that as: can't clean up, I die. Crash loop.

That's not the end; the real show comes after. I removed that file, the program started and crashed on the second socket: engine.sock. Cleared it, a third appeared: userAnalyticsOtlpHttp.sock. "Cleaning one corrupted socket exposes the next." This is not one bug — it's the same tendon rotten in three places.

Why did all three block startup? Because the code holds one rule: clean the field before starting, and if you can't, exit. For a mandatory component that rule is right. But the inference manager is an optional feature — with AI off, the engine should still run. The leftover of an optional service dragged down the whole engine.

The way out I found: rename the parent directory. The file can't be touched, but the directory's name can — after the rename the program can't find the old path, creates a fresh one, and lives. Turn off AI in settings? In some versions that switch is a decoration; the backend builds the socket anyway. The cleanest escape was downgrading to 4.69.0 — back then, switching off Beta features truly did not install the inference manager.

I filed the issue at docker/desktop-feedback (#527) with three suggestions: a socket that can't be deleted shouldn't be fatal; an optional service's failure shouldn't take down the engine; and instead of offering only "Reset to factory defaults", tell the user which file couldn't be removed. All three are cheap. All three turn "I die" into "I go around".

Later I audited my own diagnosis and found my first version had a flaw too. The issue said corrupted MFT entry; on re-examination it looks more like reparse-point orphaning — the file's record persists, the kernel context it pointed to is gone. Bug reports need self-testing too, or you become the next person who assumes.

A zero-byte file, one engine down, three places deep. Reliability is the floor: where errors are not allowed, no errors; where errors can happen, leave a side door.
