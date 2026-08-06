import os
from typing import List
from langchain_core.embeddings import Embeddings
from zhipuai import ZhipuAI

class ZhipuAIEmbeddings(Embeddings):
    """智谱 AI Embedding 适配器类（带自动分批防超限功能）"""
    def __init__(self):
        api_key = os.environ.get("ZHIPUAI_API_KEY")
        self.client = ZhipuAI(api_key=api_key)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        all_embeddings = []
        # 💡 核心修复：智谱限制一次最多发 64 条，我们设置每 32 条分批发送一次
        batch_size = 32  

        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            # 过滤掉空文本，防止智谱报错
            batch = [t if t.strip() else " " for t in batch]

            embeddings = self.client.embeddings.create(
                model="embedding-3",
                input=batch
            )
            # 把每次分批拿到的向量拼接起来
            all_embeddings.extend([item.embedding for item in embeddings.data])

        return all_embeddings

    def embed_query(self, text: str) -> List[float]:
        return self.embed_documents([text])[0]