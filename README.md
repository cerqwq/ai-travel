# ✈️ AI Travel

AI旅行工具，支持行程规划、景点推荐、预算估算。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🗺️ 行程规划
- 📍 目的地推荐
- 🎒 打包清单
- 💰 预算估算
- 🗣️ 旅行用语

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_travel import create_tools

tools = create_tools()

# 行程规划
plan = tools.plan_trip("东京", "5天", 10000, ["美食", "文化"])

# 目的地推荐
destinations = tools.recommend_destinations({"climate": "温暖"}, 5000)

# 打包清单
packing = tools.generate_packing_list("东京", "5天", ["观光", "购物"])

# 预算估算
budget = tools.estimate_budget("东京", "5天", "中档")

# 旅行用语
phrases = tools.generate_travel_phrases("日本", "日语")
```

## 📁 项目结构

```
ai-travel/
├── tools.py       # 旅行工具核心
└── README.md
```

## 📄 许可证

MIT License
