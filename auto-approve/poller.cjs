const { execSync } = require("child_process");
const { setTimeout } = require("timers/promises");

const POLL_INTERVAL_MS = 30000;
const OPENCLAW = "openclaw";
const GATEWAY_URL = "ws://host.docker.internal:18789";
const GATEWAY_TOKEN = "89a124b33a72f754bc0e9e1f02dfcf37776ea5f4dac5bd2b";

function runOpenclaw(...args) {
  const cmd = OPENCLAW + " " + args.join(" ");
  const result = execSync(cmd, {
    encoding: "utf-8",
    stdio: ["pipe", "pipe", "pipe"],
    env: Object.assign({}, process.env, { OPENCLAW_ALLOW_INSECURE_PRIVATE_WS: "1" })
  });
  const start = result.indexOf("{");
  if (start === -1) return null;
  const end = result.lastIndexOf("}");
  if (end === -1 || end < start) return null;
  try {
    return JSON.parse(result.slice(start, end + 1));
  } catch (_) {
    return null;
  }
}

async function main() {
  console.log("[auto-approve] OpenClaw device auto-approval poller started...");
  console.log("[auto-approve] Gateway: " + GATEWAY_URL);

  while (true) {
    try {
      const data = runOpenclaw("devices", "list", "--json",
        "--url", GATEWAY_URL, "--token", GATEWAY_TOKEN);
      if (!data) {
        await setTimeout(POLL_INTERVAL_MS);
        continue;
      }

      const pending = data.pending || [];
      if (pending.length === 0) {
        await setTimeout(POLL_INTERVAL_MS);
        continue;
      }

      for (const req of pending) {
        const requestId = req && req.requestId;
        if (!requestId) continue;
        try {
          execSync(OPENCLAW + " devices approve " + requestId +
            " --url " + GATEWAY_URL + " --token " + GATEWAY_TOKEN, {
            stdio: ["pipe", "pipe", "pipe"],
            env: Object.assign({}, process.env, { OPENCLAW_ALLOW_INSECURE_PRIVATE_WS: "1" })
          });
          console.log("[auto-approve] Approved: " + requestId);
        } catch (err) {
          console.error("[auto-approve] Failed " + requestId + ": " + err.message);
        }
      }
    } catch (err) {
      console.error("[auto-approve] Error: " + err.message);
    }

    await setTimeout(POLL_INTERVAL_MS);
  }
}

main().catch(function(err) {
  console.error("[auto-approve] Fatal:", err);
  process.exit(1);
});
