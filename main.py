from chatGLM import get_zhipu_respnse
from template import gen_LLM_1_prompt, gen_LLM_2_prompt, gen_LLM_3_prompt, gen_LLM_4_prompt
from database import execute_sql,schema
import json
from dotenv import load_dotenv
import time
def get_answer(question):
    """
    主函数：获取用户输入的问题，调用各个智能体进行处理，并返回最终结果。
    """
    LLM_1_prompt = gen_LLM_1_prompt(question)
    print("=============提示词开始=================")
    print("智能体一的提示语：", LLM_1_prompt)
    print("=============提示词结束=================")
    LLM_1_result = get_zhipu_respnse(LLM_1_prompt, model="GLM-4-PLUS")
    print("=============LLM回复开始================")
    print("智能体一的输出结果：", LLM_1_result)
    print("=============LLM回复结束================")
    time.sleep(5)
    LLM_2_prompt = gen_LLM_2_prompt(LLM_1_result,question,schema)
    print("=============提示词开始=================")
    print("智能体二的提示语：", LLM_2_prompt)
    print("=============提示词结束=================")
    LLM_2_result = get_zhipu_respnse(LLM_2_prompt, model="GLM-4-PLUS")
    print("=============LLM回复开始================")
    print("智能体二的输出结果：", LLM_2_result)
    print("=============LLM回复结束================")
    time.sleep(5)
    LLM_3_prompt = gen_LLM_3_prompt(question, LLM_1_result, LLM_2_result)
    print("=============提示词开始=================")
    print("智能体三的提示语：", LLM_3_prompt)
    print("=============提示词结束=================")
    LLM_3_result = get_zhipu_respnse(LLM_3_prompt, model="GLM-4-PLUS")
    print("=============LLM回复开始================")
    print("智能体三的输出结果：", LLM_3_result)
    print("=============LLM回复结束================")
    time.sleep(5)
    LLM_4_prompt = gen_LLM_4_prompt(question, LLM_1_result, LLM_2_result, LLM_3_result)
    print("=============提示词开始=================")
    print("智能体四的提示语：", LLM_4_prompt)
    print("=============提示词结束=================")
    LLM_4_result = get_zhipu_respnse(LLM_4_prompt, model="GLM-4-PLUS")
    print("=============LLM回复开始================")
    print("智能体四的输出结果：", LLM_4_result)
    print("=============LLM回复结束================")
    time.sleep(5)
    # 提取SQL语句
    sql_query = extract_sql(LLM_4_result)
    print("=============执行SQL语句================")
    if sql_query:
        # 执行SQL查询并获取结果
        result = execute_sql(sql_query)
        print("=============打印输出结果================")
        print("SQL查询结果：", result)
        ###将result转化为dataframe格式,并输出xlsx文件
        import pandas as pd
        df = pd.DataFrame(result)
        # 将DataFrame保存为Excel文件
        df.to_excel("output.xlsx", index=False)
        print("输出结果已保存为output.xlsx文件")
    # 处理SQL查询结果
    else:
        result = None
        print("没有有效的SQL查询语句")
    return result

def extract_sql(string_sql):
    """
    提取SQL语句中的表名和字段名
    """
    # 这里可以使用正则表达式或其他方法来提取表名和字段名
    # 例如：使用正则表达式匹配SELECT语句中的表名和字段名
    import re
    ##从字符串中提取json格式的内容，```json{...}```
    pattern = r'```json(.*?)```'
    match = re.search(pattern, string_sql, re.DOTALL)
    if match:
        json_string = match.group(1).strip()
        # 将提取的JSON字符串转换为Python对象
        try:
            sql_query = json.loads(json_string)
            final_sql = sql_query.get("final_sql")
            if final_sql:
                sql_query = final_sql
            else:
                print("没有找到final_sql字段")
                return None
        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")
            return None
    else:
        print("没有找到符合条件的JSON格式内容")
        return None

    return sql_query




if __name__ == "__main__":
    question = input("请输入您的问题：")
    # 示例问题
    # question = "全国的景区数据中，哪个省的景区最多？"
    get_answer(question)