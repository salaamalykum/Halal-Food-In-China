---
language:
- zh
license: mit
task_categories:
- text-retrieval
- text-generation
- question-answering
tags:
- islam
- rag
- chinese-muslim
- knowledge-base
- instruction-tuning
pretty_name: Chinese Muslim Knowledge Base
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: corpus
    path: data/corpus.parquet
  - split: rag_chunks
    path: data/rag_chunks.parquet
---

# Chinese Muslim Knowledge Base & RAG Dataset

This dataset contains 247 high-quality, human-curated articles about Chinese Muslim culture, mosques, halal food, and travel guidelines, meticulously extracted from [Salaamalykum.com](https://salaamalykum.com).

## Dataset Structure

The dataset is strictly partitioned into two splits for optimized AI training and RAG (Retrieval-Augmented Generation) pipelines:

1. **`corpus`**: The full-length articles containing raw, clean Markdown text. Best for continuous pre-training (CPT) or bulk knowledge extraction.
2. **`rag_chunks`**: The articles deterministically chunked into paragraph-level segments. Best for embedding generation, vector database ingestion, and instruction-tuning retrieval tasks.

### Data Dictionary

Both splits feature strongly typed Parquet columns optimized for SQL Data Studio filtering:

| Field | Type | Description |
|-------|------|-------------|
| `url` | `string` | The canonical source URL. In `rag_chunks`, this includes the `#chunk-id` anchor. |
| `title` | `string` | The original title of the article. |
| `text` | `string` | The sanitized Markdown content. |
| `timestamp` | `string` | ISO 8601 publication or scraping timestamp. |
| `language` | `string` | `zh-CN` (Simplified Chinese). |
| `tags` | `string` | Serialized JSON array of author-defined categorization tags. |
| `content_hash` | `string` | (Corpus only) SHA-256 hash of the `text` field for deduplication. |
| `chunk_index` | `int` | (RAG only) The zero-indexed position of the chunk in the original article. |

## Data Provenance & Cleaning Rules

All contents are strictly mirrored from the original author `yusuf908` on Salaamalykum. 

**Cleaning Rules:**
- Extracted natively from WeCenter `message` fields via Regex DOM-bypass.
- `<br>` tags normalized to `\n`.
- Embedded `<img>` attributes strictly converted to valid Markdown syntax `![image](src)`.
- Triplicate or more `\n` suppressed to `\n\n`.

**Failure Edges & Anomalies:**
- Articles containing highly complex nested tables or external iframe embeds (e.g., YouTube/Bilibili videos) will have those specific elements stripped, preserving only the textual context.
- Short form comments and discussions are excluded; this dataset focuses strictly on long-form articles.

## Embedding Atlas Architecture (Pre-computation Ready)

This dataset is fully compatible with the Hugging Face **Embedding Atlas**. The `rag_chunks` split is designed specifically for Nomic Atlas or UMAP visualization. Future iterations will include pre-computed multi-lingual embeddings (e.g., `bge-m3`) mapped directly to the `text` column to visualize the thematic clusters of Chinese Muslim geography and Halal culinary distributions.

## Human-Readable View

For the human-readable GitHub Pages deployment with a highly-indexed glassmorphism UI, visit: [https://salaamalykum.github.io/Halal-Food-In-China](https://salaamalykum.github.io/Halal-Food-In-China)
| 10家北京今年新开的餐厅：土耳其、突尼斯、胡辣汤、卤鸭、杏仁豆腐、山中小院（上篇） | [Markdown](content/10家北京今年新开的餐厅土耳其突尼斯胡辣汤卤鸭杏仁豆腐山中小院上篇.md) | [Original URL](https://salaamalykum.com/article/1626) |
| 10家北京今年新开的餐厅：土耳其、突尼斯、胡辣汤、卤鸭、杏仁豆腐、山中小院（下篇） | [Markdown](content/10家北京今年新开的餐厅土耳其突尼斯胡辣汤卤鸭杏仁豆腐山中小院下篇.md) | [Original URL](https://salaamalykum.com/article/1627) |
| 2019年西安回坊清真逛吃 | [Markdown](content/2019年西安回坊清真逛吃.md) | [Original URL](https://salaamalykum.com/article/2048) |
| 2020年昆明逛吃，拜访马聪阿訇 | [Markdown](content/2020年昆明逛吃拜访马聪阿訇.md) | [Original URL](https://salaamalykum.com/article/1942) |
| 【2024五一游】厦门寺与马尔龙新疆菜 | [Markdown](content/2024五一游厦门寺与马尔龙新疆菜.md) | [Original URL](https://salaamalykum.com/article/1665) |
| 2024北京风味清真餐厅必吃榜（上篇） | [Markdown](content/2024北京风味清真餐厅必吃榜上篇.md) | [Original URL](https://salaamalykum.com/article/1136) |
| 2024北京风味清真餐厅必吃榜（下篇） | [Markdown](content/2024北京风味清真餐厅必吃榜下篇.md) | [Original URL](https://salaamalykum.com/article/1138) |
| 2024北京风味清真餐厅必吃榜（中篇） | [Markdown](content/2024北京风味清真餐厅必吃榜中篇.md) | [Original URL](https://salaamalykum.com/article/1137) |
| 2025南京清真美食地图 | [Markdown](content/2025南京清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1126) |
| 2025广州清真美食地图 | [Markdown](content/2025广州清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1120) |
| 2025杭州清真美食地图 | [Markdown](content/2025杭州清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1115) |
| 2025青岛清真美食地图 | [Markdown](content/2025青岛清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1125) |
| 2026北京清真餐厅必吃榜 | [Markdown](content/2026北京清真餐厅必吃榜.md) | [Original URL](https://salaamalykum.com/article/1108) |
| 5月吐鲁番，古迹与美食（上篇） | [Markdown](content/5月吐鲁番古迹与美食上篇.md) | [Original URL](https://salaamalykum.com/article/2034) |
| 5月吐鲁番，古迹与美食（下篇） | [Markdown](content/5月吐鲁番古迹与美食下篇.md) | [Original URL](https://salaamalykum.com/article/2035) |
| 上海教门美食一日游 | [Markdown](content/上海教门美食一日游.md) | [Original URL](https://salaamalykum.com/article/1400) |
| 上海清真寺及清真美食地图 | [Markdown](content/上海清真寺及清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1295) |
| 世界各地的15家传统咖啡馆 | [Markdown](content/世界各地的15家传统咖啡馆.md) | [Original URL](https://salaamalykum.com/article/1619) |
| 东京清真美食地图 | [Markdown](content/东京清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1316) |
| 临夏的夜市与小吃 | [Markdown](content/临夏的夜市与小吃.md) | [Original URL](https://salaamalykum.com/article/1939) |
| 义乌又新开了很多中东餐厅（上篇） | [Markdown](content/义乌又新开了很多中东餐厅上篇.md) | [Original URL](https://salaamalykum.com/article/1656) |
| 义乌又新开了很多中东餐厅（下篇） | [Markdown](content/义乌又新开了很多中东餐厅下篇.md) | [Original URL](https://salaamalykum.com/article/1657) |
| 义乌清真美食地图 | [Markdown](content/义乌清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1297) |
| 乌鲁木齐清真美食地图 | [Markdown](content/乌鲁木齐清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1346) |
| 二十个少数族群，二十家餐厅（上篇） | [Markdown](content/二十个少数族群二十家餐厅上篇.md) | [Original URL](https://salaamalykum.com/article/2046) |
| 二十个少数族群，二十家餐厅（下篇） | [Markdown](content/二十个少数族群二十家餐厅下篇.md) | [Original URL](https://salaamalykum.com/article/2047) |
| 云南昭通清真逛吃 | [Markdown](content/云南昭通清真逛吃.md) | [Original URL](https://salaamalykum.com/article/2051) |
| 云南清真美食地图 | [Markdown](content/云南清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1354) |
| 伊斯坦布尔逛吃记 | [Markdown](content/伊斯坦布尔逛吃记.md) | [Original URL](https://salaamalykum.com/article/1843) |
| 伊朗德黑兰街头美食 | [Markdown](content/伊朗德黑兰街头美食.md) | [Original URL](https://salaamalykum.com/article/1901) |
| 元上都回回寺与锡林郭勒涮羊肉 | [Markdown](content/元上都回回寺与锡林郭勒涮羊肉.md) | [Original URL](https://salaamalykum.com/article/1514) |
| 兰州清真美食地图 | [Markdown](content/兰州清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1353) |
| 内蒙古赤峰北大寺和清真美食 | [Markdown](content/内蒙古赤峰北大寺和清真美食.md) | [Original URL](https://salaamalykum.com/article/1777) |
| 分享4家乌鲁木齐回民宴席餐厅 | [Markdown](content/分享4家乌鲁木齐回民宴席餐厅.md) | [Original URL](https://salaamalykum.com/article/1574) |
| 分享几家西安回坊的小吃 | [Markdown](content/分享几家西安回坊的小吃.md) | [Original URL](https://salaamalykum.com/article/1570) |
| 分享北京4家值得一吃的特色早餐：巴基斯坦、土耳其、内蒙古、河南 | [Markdown](content/分享北京4家值得一吃的特色早餐巴基斯坦土耳其内蒙古河南.md) | [Original URL](https://salaamalykum.com/article/1576) |
| 加拿大蒙特利尔清真寺与清真美食地图 | [Markdown](content/加拿大蒙特利尔清真寺与清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1160) |
| 北京10家值得一吃的清真馆子 | [Markdown](content/北京10家值得一吃的清真馆子.md) | [Original URL](https://salaamalykum.com/article/1621) |
| 北京10家值得一吃的清真馆子（第七期） | [Markdown](content/北京10家值得一吃的清真馆子第七期.md) | [Original URL](https://salaamalykum.com/article/1378) |
| 北京10家值得一吃的清真馆子（第二期） | [Markdown](content/北京10家值得一吃的清真馆子第二期.md) | [Original URL](https://salaamalykum.com/article/1597) |
| 北京10家值得一吃的清真馆子（第五期） | [Markdown](content/北京10家值得一吃的清真馆子第五期.md) | [Original URL](https://salaamalykum.com/article/1431) |
| 北京10家值得一吃的清真馆子（第八期） | [Markdown](content/北京10家值得一吃的清真馆子第八期.md) | [Original URL](https://salaamalykum.com/article/1368) |
| 北京10家值得一吃的清真馆子（第六期） | [Markdown](content/北京10家值得一吃的清真馆子第六期.md) | [Original URL](https://salaamalykum.com/article/1408) |
| 北京10家值得一吃的清真馆子（第四期） | [Markdown](content/北京10家值得一吃的清真馆子第四期.md) | [Original URL](https://salaamalykum.com/article/1479) |
| 北京38家外国清真馆子位置一览 | [Markdown](content/北京38家外国清真馆子位置一览.md) | [Original URL](https://salaamalykum.com/article/1602) |
| 北京51家外国清真餐厅一览 | [Markdown](content/北京51家外国清真餐厅一览.md) | [Original URL](https://salaamalykum.com/article/1494) |
| 北京65家外国清真餐厅位置 | [Markdown](content/北京65家外国清真餐厅位置.md) | [Original URL](https://salaamalykum.com/article/1376) |
| 北京Samosa中巴友谊餐厅一周年店庆 | [Markdown](content/北京Samosa中巴友谊餐厅一周年店庆.md) | [Original URL](https://salaamalykum.com/article/1633) |
| 北京午后的巴勒斯坦甜点和哈萨克奶茶 | [Markdown](content/北京午后的巴勒斯坦甜点和哈萨克奶茶.md) | [Original URL](https://salaamalykum.com/article/1439) |
| 北京清真美食地图（21） | [Markdown](content/北京清真美食地图21.md) | [Original URL](https://salaamalykum.com/article/1272) |
| 北京清真美食地图（22） | [Markdown](content/北京清真美食地图22.md) | [Original URL](https://salaamalykum.com/article/1263) |
| 北京清真美食地图（23） | [Markdown](content/北京清真美食地图23.md) | [Original URL](https://salaamalykum.com/article/1239) |
| 北京清真美食地图（24） | [Markdown](content/北京清真美食地图24.md) | [Original URL](https://salaamalykum.com/article/1236) |
| 北京清真美食地图（25） | [Markdown](content/北京清真美食地图25.md) | [Original URL](https://salaamalykum.com/article/1232) |
| 北京清真美食地图（26期） | [Markdown](content/北京清真美食地图26期.md) | [Original URL](https://salaamalykum.com/article/1231) |
| 北京清真美食地图（27期） | [Markdown](content/北京清真美食地图27期.md) | [Original URL](https://salaamalykum.com/article/1226) |
| 北京清真美食地图（28） | [Markdown](content/北京清真美食地图28.md) | [Original URL](https://salaamalykum.com/article/1223) |
| 北京清真美食地图（29） | [Markdown](content/北京清真美食地图29.md) | [Original URL](https://salaamalykum.com/article/1222) |
| 北京清真美食地图（30） | [Markdown](content/北京清真美食地图30.md) | [Original URL](https://salaamalykum.com/article/1221) |
| 北京清真美食地图（31） | [Markdown](content/北京清真美食地图31.md) | [Original URL](https://salaamalykum.com/article/1219) |
| 北京清真美食地图（32） | [Markdown](content/北京清真美食地图32.md) | [Original URL](https://salaamalykum.com/article/1214) |
| 北京清真美食地图（33） | [Markdown](content/北京清真美食地图33.md) | [Original URL](https://salaamalykum.com/article/1213) |
| 北京清真美食地图（34） | [Markdown](content/北京清真美食地图34.md) | [Original URL](https://salaamalykum.com/article/1212) |
| 北京清真美食地图（35） | [Markdown](content/北京清真美食地图35.md) | [Original URL](https://salaamalykum.com/article/1210) |
| 北京清真美食地图（36） | [Markdown](content/北京清真美食地图36.md) | [Original URL](https://salaamalykum.com/article/1200) |
| 北京清真美食地图（37） | [Markdown](content/北京清真美食地图37.md) | [Original URL](https://salaamalykum.com/article/1198) |
| 北京清真美食地图（40） | [Markdown](content/北京清真美食地图40.md) | [Original URL](https://salaamalykum.com/article/1167) |
| 北京清真美食地图（51） | [Markdown](content/北京清真美食地图51.md) | [Original URL](https://salaamalykum.com/article/1119) |
| 北京清真美食地图（55） | [Markdown](content/北京清真美食地图55.md) | [Original URL](https://salaamalykum.com/article/1112) |
| 北京清真美食地图（二十） | [Markdown](content/北京清真美食地图二十.md) | [Original URL](https://salaamalykum.com/article/1278) |
| 北京清真美食地图（十七） | [Markdown](content/北京清真美食地图十七.md) | [Original URL](https://salaamalykum.com/article/1298) |
| 北京清真美食地图（十九） | [Markdown](content/北京清真美食地图十九.md) | [Original URL](https://salaamalykum.com/article/1284) |
| 北京清真美食地图（十五） | [Markdown](content/北京清真美食地图十五.md) | [Original URL](https://salaamalykum.com/article/1304) |
| 北京清真美食地图（十八） | [Markdown](content/北京清真美食地图十八.md) | [Original URL](https://salaamalykum.com/article/1288) |
| 北京清真美食地图（十六） | [Markdown](content/北京清真美食地图十六.md) | [Original URL](https://salaamalykum.com/article/1302) |
| 北京清真美食地图（十四） | [Markdown](content/北京清真美食地图十四.md) | [Original URL](https://salaamalykum.com/article/1313) |
| 北京清真美食地图（第38期） | [Markdown](content/北京清真美食地图第38期.md) | [Original URL](https://salaamalykum.com/article/1175) |
| 北京清真美食地图（第41期） | [Markdown](content/北京清真美食地图第41期.md) | [Original URL](https://salaamalykum.com/article/1164) |
| 北京清真美食地图（第42期） | [Markdown](content/北京清真美食地图第42期.md) | [Original URL](https://salaamalykum.com/article/1163) |
| 北京清真美食地图（第43期） | [Markdown](content/北京清真美食地图第43期.md) | [Original URL](https://salaamalykum.com/article/1154) |
| 北京清真美食地图（第44期） | [Markdown](content/北京清真美食地图第44期.md) | [Original URL](https://salaamalykum.com/article/1151) |
| 北京清真美食地图（第45期） | [Markdown](content/北京清真美食地图第45期.md) | [Original URL](https://salaamalykum.com/article/1149) |
| 北京清真美食地图（第47期） | [Markdown](content/北京清真美食地图第47期.md) | [Original URL](https://salaamalykum.com/article/1130) |
| 北京清真美食地图（第48期） | [Markdown](content/北京清真美食地图第48期.md) | [Original URL](https://salaamalykum.com/article/1128) |
| 北京清真美食地图（第49期） | [Markdown](content/北京清真美食地图第49期.md) | [Original URL](https://salaamalykum.com/article/1122) |
| 北京清真美食地图（第50期） | [Markdown](content/北京清真美食地图第50期.md) | [Original URL](https://salaamalykum.com/article/1121) |
| 北京清真美食地图（第52期） | [Markdown](content/北京清真美食地图第52期.md) | [Original URL](https://salaamalykum.com/article/1117) |
| 北京清真美食地图（第53期） | [Markdown](content/北京清真美食地图第53期.md) | [Original URL](https://salaamalykum.com/article/1114) |
| 北京清真美食地图（第54期） | [Markdown](content/北京清真美食地图第54期.md) | [Original URL](https://salaamalykum.com/article/1113) |
| 北京清真美食地图（第56期） | [Markdown](content/北京清真美食地图第56期.md) | [Original URL](https://salaamalykum.com/article/1106) |
| 北京特色清真美食地图（十三） | [Markdown](content/北京特色清真美食地图十三.md) | [Original URL](https://salaamalykum.com/article/1319) |
| 北京特色清真餐饮指南（七） | [Markdown](content/北京特色清真餐饮指南七.md) | [Original URL](https://salaamalykum.com/article/1335) |
| 北京特色清真餐饮指南（九） | [Markdown](content/北京特色清真餐饮指南九.md) | [Original URL](https://salaamalykum.com/article/1331) |
| 北京特色清真餐饮指南（五） | [Markdown](content/北京特色清真餐饮指南五.md) | [Original URL](https://salaamalykum.com/article/1338) |
| 北京特色清真餐饮指南（八） | [Markdown](content/北京特色清真餐饮指南八.md) | [Original URL](https://salaamalykum.com/article/1333) |
| 北京特色清真餐饮指南（六） | [Markdown](content/北京特色清真餐饮指南六.md) | [Original URL](https://salaamalykum.com/article/1337) |
| 北京特色清真餐饮指南（十） | [Markdown](content/北京特色清真餐饮指南十.md) | [Original URL](https://salaamalykum.com/article/1326) |
| 北京特色清真餐饮指南（十一） | [Markdown](content/北京特色清真餐饮指南十一.md) | [Original URL](https://salaamalykum.com/article/1323) |
| 北京特色清真餐饮指南（十二） | [Markdown](content/北京特色清真餐饮指南十二.md) | [Original URL](https://salaamalykum.com/article/1322) |
| 【北京特色清真餐饮指南（含最全外国餐厅）】（一） | [Markdown](content/北京特色清真餐饮指南含最全外国餐厅一.md) | [Original URL](https://salaamalykum.com/article/1361) |
| 【北京特色清真餐饮指南（含最全外国餐厅）】（三） | [Markdown](content/北京特色清真餐饮指南含最全外国餐厅三.md) | [Original URL](https://salaamalykum.com/article/1351) |
| 【北京特色清真餐饮指南（含最全外国餐厅）】（二） | [Markdown](content/北京特色清真餐饮指南含最全外国餐厅二.md) | [Original URL](https://salaamalykum.com/article/1360) |
| 北京特色清真餐饮指南（四） | [Markdown](content/北京特色清真餐饮指南四.md) | [Original URL](https://salaamalykum.com/article/1339) |
| 北京的三家土库曼斯坦餐厅 | [Markdown](content/北京的三家土库曼斯坦餐厅.md) | [Original URL](https://salaamalykum.com/article/1379) |
| 南京清真美食地图 | [Markdown](content/南京清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1336) |
| 印尼中爪哇逛吃：三宝垄、梭罗、古突士 | [Markdown](content/印尼中爪哇逛吃三宝垄梭罗古突士.md) | [Original URL](https://salaamalykum.com/article/1848) |
| 印尼首都雅加达逛吃记 | [Markdown](content/印尼首都雅加达逛吃记.md) | [Original URL](https://salaamalykum.com/article/1852) |
| 台湾清真美食回忆（一）：台北的天津与保定清真馆 | [Markdown](content/台湾清真美食回忆一台北的天津与保定清真馆.md) | [Original URL](https://salaamalykum.com/article/1673) |
| 台湾清真美食回忆（二）：台湾各地的清真馆子 | [Markdown](content/台湾清真美食回忆二台湾各地的清真馆子.md) | [Original URL](https://salaamalykum.com/article/1672) |
| 各地清真小吃荟萃（中国西部篇）（上篇） | [Markdown](content/各地清真小吃荟萃中国西部篇上篇.md) | [Original URL](https://salaamalykum.com/article/1951) |
| 各地清真小吃荟萃（中国西部篇）（下篇） | [Markdown](content/各地清真小吃荟萃中国西部篇下篇.md) | [Original URL](https://salaamalykum.com/article/1953) |
| 各地清真小吃荟萃（中国西部篇）（中篇） | [Markdown](content/各地清真小吃荟萃中国西部篇中篇.md) | [Original URL](https://salaamalykum.com/article/1952) |
| 吉隆坡清真美食地图（上篇） | [Markdown](content/吉隆坡清真美食地图上篇.md) | [Original URL](https://salaamalykum.com/article/1173) |
| 吉隆坡清真美食地图（下篇） | [Markdown](content/吉隆坡清真美食地图下篇.md) | [Original URL](https://salaamalykum.com/article/1174) |
| 吉隆坡清真美食地图（第6期） | [Markdown](content/吉隆坡清真美食地图第6期.md) | [Original URL](https://salaamalykum.com/article/1111) |
| 吉隆坡清真美食地图（第7期） | [Markdown](content/吉隆坡清真美食地图第7期.md) | [Original URL](https://salaamalykum.com/article/1110) |
| 吉隆坡清真美食地图（第8期） | [Markdown](content/吉隆坡清真美食地图第8期.md) | [Original URL](https://salaamalykum.com/article/1109) |
| 吉隆坡清真美食地图（第9期） | [Markdown](content/吉隆坡清真美食地图第9期.md) | [Original URL](https://salaamalykum.com/article/1107) |
| 吉隆坡清真美食地图（第三期） | [Markdown](content/吉隆坡清真美食地图第三期.md) | [Original URL](https://salaamalykum.com/article/1145) |
| 吉隆坡清真美食地图（第二期） | [Markdown](content/吉隆坡清真美食地图第二期.md) | [Original URL](https://salaamalykum.com/article/1146) |
| 吉隆坡清真美食地图（第五期） | [Markdown](content/吉隆坡清真美食地图第五期.md) | [Original URL](https://salaamalykum.com/article/1129) |
| 吉隆坡清真美食地图（第四期） | [Markdown](content/吉隆坡清真美食地图第四期.md) | [Original URL](https://salaamalykum.com/article/1141) |
| 周末在北京音乐美食节吃土耳其与巴基斯坦美食 | [Markdown](content/周末在北京音乐美食节吃土耳其与巴基斯坦美食.md) | [Original URL](https://salaamalykum.com/article/1395) |
| 周末在朝阳公园国际美食嘉年华品尝世界美食 | [Markdown](content/周末在朝阳公园国际美食嘉年华品尝世界美食.md) | [Original URL](https://salaamalykum.com/article/1472) |
| 品尝世界各地的饮料（马来西亚、新加坡、印尼篇） | [Markdown](content/品尝世界各地的饮料马来西亚新加坡印尼篇.md) | [Original URL](https://salaamalykum.com/article/1608) |
| 品尝包头的回民美食 | [Markdown](content/品尝包头的回民美食.md) | [Original URL](https://salaamalykum.com/article/1446) |
| 品尝缅族教门菜——在仰光遇见缅族朵斯提 | [Markdown](content/品尝缅族教门菜在仰光遇见缅族朵斯提.md) | [Original URL](https://salaamalykum.com/article/1424) |
| 喀山鞑靼人的特色糕点 | [Markdown](content/喀山鞑靼人的特色糕点.md) | [Original URL](https://salaamalykum.com/article/1856) |
| 四川松潘的回民小吃 | [Markdown](content/四川松潘的回民小吃.md) | [Original URL](https://salaamalykum.com/article/1427) |
| 四川绵阳、德阳清真美食地图 | [Markdown](content/四川绵阳德阳清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1177) |
| 四川都江堰的古寺与美食 | [Markdown](content/四川都江堰的古寺与美食.md) | [Original URL](https://salaamalykum.com/article/1660) |
| 土耳其埃迪尔内、布尔萨、科尼亚美食之旅 | [Markdown](content/土耳其埃迪尔内布尔萨科尼亚美食之旅.md) | [Original URL](https://salaamalykum.com/article/1975) |
| 在义乌品尝外国美食 | [Markdown](content/在义乌品尝外国美食.md) | [Original URL](https://salaamalykum.com/article/2109) |
| 在亚庇逛菲律宾市集、吃海南美食 | [Markdown](content/在亚庇逛菲律宾市集吃海南美食.md) | [Original URL](https://salaamalykum.com/article/1589) |
| 在克里米亚鞑靼人的故都逛吃 | [Markdown](content/在克里米亚鞑靼人的故都逛吃.md) | [Original URL](https://salaamalykum.com/article/2020) |
| 在北京JM咖啡烘焙店感受圣诞氛围 | [Markdown](content/在北京JM咖啡烘焙店感受圣诞氛围.md) | [Original URL](https://salaamalykum.com/article/1413) |
| 在北京参加地中海美食节，品尝巴勒斯坦国菜与埃及开斋特饮 | [Markdown](content/在北京参加地中海美食节品尝巴勒斯坦国菜与埃及开斋特饮.md) | [Original URL](https://salaamalykum.com/article/1474) |
| 在北京品尝马来西亚美食——2024北京马来西亚节 | [Markdown](content/在北京品尝马来西亚美食2024北京马来西亚节.md) | [Original URL](https://salaamalykum.com/article/1613) |
| 在北京外交公寓品尝马尔代夫、埃及小吃 | [Markdown](content/在北京外交公寓品尝马尔代夫埃及小吃.md) | [Original URL](https://salaamalykum.com/article/1527) |
| 在南印度古城海德拉巴逛吃 | [Markdown](content/在南印度古城海德拉巴逛吃.md) | [Original URL](https://salaamalykum.com/article/1907) |
| 在印尼大使馆品尝正宗印尼美食 | [Markdown](content/在印尼大使馆品尝正宗印尼美食.md) | [Original URL](https://salaamalykum.com/article/1485) |
| 在呼和浩特大寺吃早餐 | [Markdown](content/在呼和浩特大寺吃早餐.md) | [Original URL](https://salaamalykum.com/article/1476) |
| 在四川乐山和峨眉山吃跷脚牛肉 | [Markdown](content/在四川乐山和峨眉山吃跷脚牛肉.md) | [Original URL](https://salaamalykum.com/article/1661) |
| 在国际邻里节品尝伊朗、阿塞拜疆、马尔代夫美食 | [Markdown](content/在国际邻里节品尝伊朗阿塞拜疆马尔代夫美食.md) | [Original URL](https://salaamalykum.com/article/1616) |
| 在天津吃阿拉伯菜：叙利亚、也门、突尼斯、阿尔及利亚 | [Markdown](content/在天津吃阿拉伯菜叙利亚也门突尼斯阿尔及利亚.md) | [Original URL](https://salaamalykum.com/article/1573) |
| 在成都土桥品尝川味美食 | [Markdown](content/在成都土桥品尝川味美食.md) | [Original URL](https://salaamalykum.com/article/1658) |
| 在新加坡吃娘惹菜 | [Markdown](content/在新加坡吃娘惹菜.md) | [Original URL](https://salaamalykum.com/article/1704) |
| 在汉中仙隐寺吃羊肉 | [Markdown](content/在汉中仙隐寺吃羊肉.md) | [Original URL](https://salaamalykum.com/article/2069) |
| 在福州礼主麻：福州寺、筛海墓、宋元教门石刻、土耳其餐厅 | [Markdown](content/在福州礼主麻福州寺筛海墓宋元教门石刻土耳其餐厅.md) | [Original URL](https://salaamalykum.com/article/1663) |
| 在莫斯科吃中亚菜 | [Markdown](content/在莫斯科吃中亚菜.md) | [Original URL](https://salaamalykum.com/article/2025) |
| 在郑和出使过的吉兰丹港吃清真中餐 | [Markdown](content/在郑和出使过的吉兰丹港吃清真中餐.md) | [Original URL](https://salaamalykum.com/article/1498) |
| 在马来西亚、新加坡、文莱吃清真海南餐厅（上篇） | [Markdown](content/在马来西亚新加坡文莱吃清真海南餐厅上篇.md) | [Original URL](https://salaamalykum.com/article/1369) |
| 在马来西亚、新加坡、文莱吃清真海南餐厅（下篇） | [Markdown](content/在马来西亚新加坡文莱吃清真海南餐厅下篇.md) | [Original URL](https://salaamalykum.com/article/1370) |
| 在马来西亚新山和吉隆坡吃娘惹菜 | [Markdown](content/在马来西亚新山和吉隆坡吃娘惹菜.md) | [Original URL](https://salaamalykum.com/article/1697) |
| 塔什干城逛吃记 | [Markdown](content/塔什干城逛吃记.md) | [Original URL](https://salaamalykum.com/article/1853) |
| 夏日呼和浩特清真逛吃 | [Markdown](content/夏日呼和浩特清真逛吃.md) | [Original URL](https://salaamalykum.com/article/2097) |
| 大珠三角地区清真美食地图（粤、港、澳） | [Markdown](content/大珠三角地区清真美食地图粤港澳.md) | [Original URL](https://salaamalykum.com/article/1342) |
| 大理清真美食地图（上篇） | [Markdown](content/大理清真美食地图上篇.md) | [Original URL](https://salaamalykum.com/article/1189) |
| 大理清真美食地图（下篇） | [Markdown](content/大理清真美食地图下篇.md) | [Original URL](https://salaamalykum.com/article/1191) |
| 大理清真美食地图（中篇） | [Markdown](content/大理清真美食地图中篇.md) | [Original URL](https://salaamalykum.com/article/1190) |
| 大连清真美食地图（二） | [Markdown](content/大连清真美食地图二.md) | [Original URL](https://salaamalykum.com/article/1303) |
| 大马士革奥斯曼大宅酒店与餐厅 | [Markdown](content/大马士革奥斯曼大宅酒店与餐厅.md) | [Original URL](https://salaamalykum.com/article/1393) |
| 大马士革老城逛吃 | [Markdown](content/大马士革老城逛吃.md) | [Original URL](https://salaamalykum.com/article/1415) |
| 天津清真美食地图 | [Markdown](content/天津清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1359) |
| 天津清真美食地图（三） | [Markdown](content/天津清真美食地图三.md) | [Original URL](https://salaamalykum.com/article/1314) |
| 天津清真美食地图（二） | [Markdown](content/天津清真美食地图二.md) | [Original URL](https://salaamalykum.com/article/1340) |
| 天津清真美食地图（五） | [Markdown](content/天津清真美食地图五.md) | [Original URL](https://salaamalykum.com/article/1123) |
| 天津清真美食地图（四） | [Markdown](content/天津清真美食地图四.md) | [Original URL](https://salaamalykum.com/article/1220) |
| 天津的清真美食还是太全面了：意面、烧鸟、也门大饼、瑞士芝士火锅、饭团 | [Markdown](content/天津的清真美食还是太全面了意面烧鸟也门大饼瑞士芝士火锅饭团.md) | [Original URL](https://salaamalykum.com/article/1495) |
| 天津遛娃下馆子：也门菜、阿尔及利亚甜点、肠粉、日料、菱角汤 | [Markdown](content/天津遛娃下馆子也门菜阿尔及利亚甜点肠粉日料菱角汤.md) | [Original URL](https://salaamalykum.com/article/1632) |
| 太原的清真古寺与清真美食 | [Markdown](content/太原的清真古寺与清真美食.md) | [Original URL](https://salaamalykum.com/article/2056) |
| 山东清真美食地图 | [Markdown](content/山东清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1341) |
| 山海之间——从怀柔农家乐到滨海西餐厅 | [Markdown](content/山海之间从怀柔农家乐到滨海西餐厅.md) | [Original URL](https://salaamalykum.com/article/1625) |
| 巴蜀地区（陇南、广元、成都、重庆）清真美食地图 | [Markdown](content/巴蜀地区陇南广元成都重庆清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1357) |
| 帝都特色清真美食大全（上篇） | [Markdown](content/帝都特色清真美食大全上篇.md) | [Original URL](https://salaamalykum.com/article/1329) |
| 帝都特色清真美食大全（下篇） | [Markdown](content/帝都特色清真美食大全下篇.md) | [Original URL](https://salaamalykum.com/article/1330) |
| 帝都特色清真美食大全（补充版） | [Markdown](content/帝都特色清真美食大全补充版.md) | [Original URL](https://salaamalykum.com/article/1327) |
| 广州小北的夜与日：摩洛哥菜与广式早茶 | [Markdown](content/广州小北的夜与日摩洛哥菜与广式早茶.md) | [Original URL](https://salaamalykum.com/article/1445) |
| 开封的寺门汤锅与清真夜市 | [Markdown](content/开封的寺门汤锅与清真夜市.md) | [Original URL](https://salaamalykum.com/article/2041) |
| 开斋节在即，献上一幅最新最全的牛街美食地图（上篇） | [Markdown](content/开斋节在即献上一幅最新最全的牛街美食地图上篇.md) | [Original URL](https://salaamalykum.com/article/1324) |
| 开斋节在即，献上一幅最新最全的牛街美食地图（下篇） | [Markdown](content/开斋节在即献上一幅最新最全的牛街美食地图下篇.md) | [Original URL](https://salaamalykum.com/article/1325) |
| 开罗老城逛吃（上篇） | [Markdown](content/开罗老城逛吃上篇.md) | [Original URL](https://salaamalykum.com/article/1718) |
| 开罗老城逛吃（下篇） | [Markdown](content/开罗老城逛吃下篇.md) | [Original URL](https://salaamalykum.com/article/1719) |
| 张家口、宣化的清真寺与清真美食（上篇） | [Markdown](content/张家口宣化的清真寺与清真美食上篇.md) | [Original URL](https://salaamalykum.com/article/2057) |
| 张家口、宣化的清真寺与清真美食（下篇） | [Markdown](content/张家口宣化的清真寺与清真美食下篇.md) | [Original URL](https://salaamalykum.com/article/2058) |
| 怀柔山里的鸦儿李记小院 | [Markdown](content/怀柔山里的鸦儿李记小院.md) | [Original URL](https://salaamalykum.com/article/1647) |
| 成都清真美食地图（上篇） | [Markdown](content/成都清真美食地图上篇.md) | [Original URL](https://salaamalykum.com/article/1192) |
| 成都清真美食地图（下篇） | [Markdown](content/成都清真美食地图下篇.md) | [Original URL](https://salaamalykum.com/article/1193) |
| 我在各地吃粉面（南方篇） | [Markdown](content/我在各地吃粉面南方篇.md) | [Original URL](https://salaamalykum.com/article/1930) |
| 我在各地吃粉面（国外篇） | [Markdown](content/我在各地吃粉面国外篇.md) | [Original URL](https://salaamalykum.com/article/1929) |
| 我在各地吃面条（北方篇） | [Markdown](content/我在各地吃面条北方篇.md) | [Original URL](https://salaamalykum.com/article/1931) |
| 承德的三座古寺与回民美食 | [Markdown](content/承德的三座古寺与回民美食.md) | [Original URL](https://salaamalykum.com/article/1500) |
| 承德的清真寺与清真美食 | [Markdown](content/承德的清真寺与清真美食.md) | [Original URL](https://salaamalykum.com/article/2063) |
| 按北京各城区分类的清真美食地图（朝阳群众有口福了） | [Markdown](content/按北京各城区分类的清真美食地图朝阳群众有口福了.md) | [Original URL](https://salaamalykum.com/article/1318) |
| 撒马尔罕古城逛吃记 | [Markdown](content/撒马尔罕古城逛吃记.md) | [Original URL](https://salaamalykum.com/article/1854) |
| 日本清真美食地图 | [Markdown](content/日本清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1352) |
| 昆明向南行（七）蒙自过桥米线、昆明顺城街 | [Markdown](content/昆明向南行七蒙自过桥米线昆明顺城街.md) | [Original URL](https://salaamalykum.com/article/1941) |
| 曼谷清真之旅——吃住篇 | [Markdown](content/曼谷清真之旅吃住篇.md) | [Original URL](https://salaamalykum.com/article/1767) |
| 最近新吃的10家北京馆子推荐 | [Markdown](content/最近新吃的10家北京馆子推荐.md) | [Original URL](https://salaamalykum.com/article/1492) |
| 栽娜卜的新疆家常菜谱​ | [Markdown](content/栽娜卜的新疆家常菜谱.md) | [Original URL](https://salaamalykum.com/article/1938) |
| 毕业十年回武汉（上）：江岸寺坊、华师大、武昌美食 | [Markdown](content/毕业十年回武汉上江岸寺坊华师大武昌美食.md) | [Original URL](https://salaamalykum.com/article/1679) |
| 毕业十年回武汉（下）：马四巴巴坟、土耳其咖啡、法图麦饭庄 | [Markdown](content/毕业十年回武汉下马四巴巴坟土耳其咖啡法图麦饭庄.md) | [Original URL](https://salaamalykum.com/article/1677) |
| 江浙沪清真美食地图 | [Markdown](content/江浙沪清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1347) |
| 江苏宿迁：洋河镇古寺与泗阳马家饭庄 | [Markdown](content/江苏宿迁洋河镇古寺与泗阳马家饭庄.md) | [Original URL](https://salaamalykum.com/article/1530) |
| 江苏淮安河下古镇：古寺、茶馓、左宝贵墓 | [Markdown](content/江苏淮安河下古镇古寺茶馓左宝贵墓.md) | [Original URL](https://salaamalykum.com/article/1528) |
| 江苏淮安清江古寺与淮扬教门菜 | [Markdown](content/江苏淮安清江古寺与淮扬教门菜.md) | [Original URL](https://salaamalykum.com/article/1519) |
| 江苏盐城访古寺与本地回民美食 | [Markdown](content/江苏盐城访古寺与本地回民美食.md) | [Original URL](https://salaamalykum.com/article/1529) |
| 河北清真美食地图 | [Markdown](content/河北清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1358) |
| 河南清真美食地图 | [Markdown](content/河南清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1356) |
| 泰国大城府逛吃：清真农家乐与拱北乜贴席 | [Markdown](content/泰国大城府逛吃清真农家乐与拱北乜贴席.md) | [Original URL](https://salaamalykum.com/article/1437) |
| 泰国普吉岛清真美食地图 | [Markdown](content/泰国普吉岛清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1350) |
| 海南清真美食地图 | [Markdown](content/海南清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1343) |
| 湖北清真美食地图 | [Markdown](content/湖北清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1348) |
| 湖南邵阳回民美食 | [Markdown](content/湖南邵阳回民美食.md) | [Original URL](https://salaamalykum.com/article/1362) |
| 爪哇古城日惹的美食 | [Markdown](content/爪哇古城日惹的美食.md) | [Original URL](https://salaamalykum.com/article/1847) |
| 甘肃天水的老三片、呱呱、浆水面 | [Markdown](content/甘肃天水的老三片呱呱浆水面.md) | [Original URL](https://salaamalykum.com/article/1423) |
| 甘肃秦安清代古寺与特色蒜面 | [Markdown](content/甘肃秦安清代古寺与特色蒜面.md) | [Original URL](https://salaamalykum.com/article/1564) |
| 疫情过后的清真餐饮幸存者——2020北京风味清真餐厅必吃榜 | [Markdown](content/疫情过后的清真餐饮幸存者2020北京风味清真餐厅必吃榜.md) | [Original URL](https://salaamalykum.com/article/1289) |
| 【看展记】天津西北角回民“花活马家”和“刻砖刘”精美的砖雕作品 | [Markdown](content/看展记天津西北角回民花活马家和刻砖刘精美的砖雕作品.md) | [Original URL](https://salaamalykum.com/article/1606) |
| 秋日天津逛吃：叙利亚菜、罗氏虾、黄汤拉面、土耳其馆子、新疆鲜奶冰淇淋 | [Markdown](content/秋日天津逛吃叙利亚菜罗氏虾黄汤拉面土耳其馆子新疆鲜奶冰淇淋.md) | [Original URL](https://salaamalykum.com/article/1605) |
| 突尼斯苏塞世遗老城逛吃 | [Markdown](content/突尼斯苏塞世遗老城逛吃.md) | [Original URL](https://salaamalykum.com/article/1422) |
| 突尼斯麦地那老城：历史民宿、美食、购物（上篇） | [Markdown](content/突尼斯麦地那老城历史民宿美食购物上篇.md) | [Original URL](https://salaamalykum.com/article/1531) |
| 突尼斯麦地那老城：历史民宿、美食、购物（下篇） | [Markdown](content/突尼斯麦地那老城历史民宿美食购物下篇.md) | [Original URL](https://salaamalykum.com/article/1532) |
| 【端午辽宁行】凤城古寺与丹东美食 | [Markdown](content/端午辽宁行凤城古寺与丹东美食.md) | [Original URL](https://salaamalykum.com/article/1642) |
| 【端午辽宁行】沈阳逛早市，新民访古寺 | [Markdown](content/端午辽宁行沈阳逛早市新民访古寺.md) | [Original URL](https://salaamalykum.com/article/1654) |
| 约旦首都安曼老城逛吃 | [Markdown](content/约旦首都安曼老城逛吃.md) | [Original URL](https://salaamalykum.com/article/1396) |
| 纽约、亚特兰大、西雅图清真美食地图 | [Markdown](content/纽约亚特兰大西雅图清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1334) |
| 缅甸仰光的回民寺坊与回民美食 | [Markdown](content/缅甸仰光的回民寺坊与回民美食.md) | [Original URL](https://salaamalykum.com/article/1444) |
| 羊肉烧麦、糯米烧麦和广式烧麦都很好吃 | [Markdown](content/羊肉烧麦糯米烧麦和广式烧麦都很好吃.md) | [Original URL](https://salaamalykum.com/article/1599) |
| 萨拉热窝的波斯尼亚克美食 | [Markdown](content/萨拉热窝的波斯尼亚克美食.md) | [Original URL](https://salaamalykum.com/article/1730) |
| 西宁清真美食地图 | [Markdown](content/西宁清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1328) |
| 西宁清真美食地图（二） | [Markdown](content/西宁清真美食地图二.md) | [Original URL](https://salaamalykum.com/article/1283) |
| 西藏清真美食地图 | [Markdown](content/西藏清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1355) |
| 西贡滨城市场和附近的清真街 | [Markdown](content/西贡滨城市场和附近的清真街.md) | [Original URL](https://salaamalykum.com/article/1083) |
| 赫达·莫理循拍摄的民国时期的烤肉宛 | [Markdown](content/赫达莫理循拍摄的民国时期的烤肉宛.md) | [Original URL](https://salaamalykum.com/article/1921) |
| 越南河内努尔清真寺与清真牛肉河粉 | [Markdown](content/越南河内努尔清真寺与清真牛肉河粉.md) | [Original URL](https://salaamalykum.com/article/1438) |
| 越南胡志明、芽庄清真美食地图 | [Markdown](content/越南胡志明芽庄清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1321) |
| 辽宁绥中的清真寺与清真小吃 | [Markdown](content/辽宁绥中的清真寺与清真小吃.md) | [Original URL](https://salaamalykum.com/article/2062) |
| 鄂尔多斯、包头、呼和浩特清真美食地图 | [Markdown](content/鄂尔多斯包头呼和浩特清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1344) |
| 重庆清真美食之旅——原来毛肚火锅也跟回民有关 | [Markdown](content/重庆清真美食之旅原来毛肚火锅也跟回民有关.md) | [Original URL](https://salaamalykum.com/article/1294) |
| 长春、哈尔滨、沈阳清真美食地图 | [Markdown](content/长春哈尔滨沈阳清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1345) |
| 长沙唯一的湖南本地回民炒菜馆 | [Markdown](content/长沙唯一的湖南本地回民炒菜馆.md) | [Original URL](https://salaamalykum.com/article/1365) |
| 阿塞拜疆巴库老城的木卡姆与美食 | [Markdown](content/阿塞拜疆巴库老城的木卡姆与美食.md) | [Original URL](https://salaamalykum.com/article/1846) |
| 霹雳苏丹皇城与热闹的马来夜市 | [Markdown](content/霹雳苏丹皇城与热闹的马来夜市.md) | [Original URL](https://salaamalykum.com/article/1695) |
| 马六甲古城逛吃记（食宿篇） | [Markdown](content/马六甲古城逛吃记食宿篇.md) | [Original URL](https://salaamalykum.com/article/1617) |
| 马来西亚槟城的华人清真美食 | [Markdown](content/马来西亚槟城的华人清真美食.md) | [Original URL](https://salaamalykum.com/article/1955) |
| 马来西亚清真美食地图 | [Markdown](content/马来西亚清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1349) |
