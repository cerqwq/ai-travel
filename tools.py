"""
AI Travel - AI旅行工具
支持行程规划、景点推荐、预算估算
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AITravelTools:
    """
    AI旅行工具
    支持：规划、推荐、预算
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def plan_trip(self, destination: str, duration: str, budget: float, interests: List[str]) -> Dict:
        """规划旅行"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        interests_text = ", ".join(interests)

        prompt = f"""请规划{destination}的{duration}旅行：

预算：{budget}元
兴趣：{interests_text}

请返回JSON格式：
{{
    "itinerary": [
        {{"day": "第一天", "activities": [{{"time": "时间", "activity": "活动", "location": "地点", "cost": "费用"}}]}}
    ],
    "accommodation": "住宿建议",
    "transportation": "交通建议",
    "total_estimated_cost": "预估总费用",
    "tips": ["旅行贴士"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"plan": content}

    def recommend_destinations(self, preferences: Dict, budget: float) -> List[Dict]:
        """推荐目的地"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        prefs_text = json.dumps(preferences, ensure_ascii=False)

        prompt = f"""请根据以下偏好推荐旅行目的地：

偏好：{prefs_text}
预算：{budget}元

请返回JSON格式：
[
    {{"destination": "目的地", "reason": "推荐原因", "best_time": "最佳时间", "estimated_cost": "预估费用"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"recommendations": content}]

    def generate_packing_list(self, destination: str, duration: str, activities: List[str]) -> List[Dict]:
        """生成打包清单"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        activities_text = ", ".join(activities)

        prompt = f"""请为{destination}的{duration}旅行生成打包清单：

活动：{activities_text}

请返回JSON格式：
[
    {{"category": "类别", "items": ["物品1", "物品2"]}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"packing_list": content}]

    def estimate_budget(self, destination: str, duration: str, style: str) -> Dict:
        """估算预算"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请估算{destination}的{duration}旅行预算：

旅行风格：{style}

请返回JSON格式：
{{
    "categories": {{"category": "费用"}},
    "total": "总费用",
    "tips": ["省钱建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"budget": content}

    def generate_travel_phrases(self, destination: str, language: str) -> Dict:
        """生成旅行用语"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请生成在{destination}旅行常用的{language}短语：

请返回JSON格式：
{{
    "greetings": [{{"phrase": "短语", "pronunciation": "发音", "meaning": "含义"}}],
    "dining": [{{"phrase": "短语", "pronunciation": "发音", "meaning": "含义"}}],
    "transportation": [{{"phrase": "短语", "pronunciation": "发音", "meaning": "含义"}}],
    "emergency": [{{"phrase": "短语", "pronunciation": "发音", "meaning": "含义"}}]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"phrases": content}


def create_tools(**kwargs) -> AITravelTools:
    """创建旅行工具"""
    return AITravelTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Travel Tools")
    print()

    # 测试
    plan = tools.plan_trip("东京", "5天", 10000, ["美食", "文化", "购物"])
    print(json.dumps(plan, ensure_ascii=False, indent=2))
