---
title: "Excel Is Two-Dimensional"
description: "Excel uses rows and columns because two-dimensional tables are the easiest structure for the human eye and brain to understand. But the real world is not two-dimensional."
slug: "excel是二维的"
tags: ["技术", "数据", "工具"]
draft: false
translationKey: "excel是二维的"
---

Excel uses rows and columns because two-dimensional tables are the easiest structure for the human eye and brain to understand. But the real world is not two-dimensional.

Take mobile phone recycling as an example. The factors that affect the value of a single phone include at least a dozen dimensions: model, condition, battery, channel, time ofbuyback, weather, market sentiment, new product launches, inventory levels, profit margin, turnover days. These dimensions also interact with each other: weather affectsbuyback price, buyback price determines profit margin, profit margin relates to inventory strategy. Excel cannot naturally express this kind of multi-dimensional relational network.

At its core, the problem is that the human brain is not wired to process high-dimensional information, but computers are. Traditional software forces the high-dimensional world into a two-dimensional table so that humans can understand it. The data is still there, and the numbers are still there, but the relationships are broken and the patterns are invisible.

Systems like Palantir take the opposite approach. They do not flatten the data. They preserve the multi-dimensional network structure. All entities are treated as nodes, and all relationships between entities are treated as connections. The computer is responsible for storing andrelating all the dimensions. Humans only need to query when necessary.

Excel flattens the world so humans can see it. Palantir preserves the world as it is and lets the computer understand it.

The practical lesson for real business is this: when you need to make a decision based on multiple dimensions, do not try to cram everything into a single spreadsheet. Use a networked data structure to preserve the complete set of relationships. Your brain cannot simultaneously process a dozen dimensions, but a computer can store the relationships, find the patterns, and give you the answer.
