
def gen_LLM_1_prompt(user_question):
    """
    智能体一：意图识别
    给定一个自然语言问题，识别出用户的意图。
    """
    LLM_1 = f"""
    -- 用户问题：{user_question} -- 这里需要插入用户的问题
    请逐步分析用户问题，完成以下步骤：
    1. 识别问题中的关键动词（如查询、统计、修改等）
    2. 提取问题中的核心实体（如客户、订单、产品等）
    3. 分析可能的操作类型（SELECT/UPDATE/INSERT/DELETE）
    4. 列出所有可能的意图（不少于2个）
    5. 通过对比验证最终确定最匹配的意图
    自我检查：如果意图存在歧义，是否需要进一步澄清？
    最终输出格式：JSON {{"intent": "", "entities": [], "operation": ""}}
    """
    return LLM_1

def gen_LLM_2_prompt(LLM_1_result, quetion,schema):
    """
    智能体二：数据库表匹配
    根据用户的意图，匹配出相应的数据库表和字段。
    """
    LLM_2 = f"""
    -- 用户问题：{quetion} -- 这里需要插入用户的问题
    -- 识别意图：{LLM_1_result} -- 这里需要插入智能体一的输出结果
    -- 数据库Schema：{schema} -- 这里需要插入数据库Schema的描述
    根据已识别的意图执行以下步骤：
    1. 回忆数据库Schema中所有相关表（不少于3个候选）
    2. 分析实体与表字段的映射关系
    3. 验证表间关联关系（主外键约束）
    4. 列出所有可能的表组合方案
    5. 选择最优方案并说明理由
    自我检查：是否存在更简洁/更高效的表连接方式？
    最终输出格式：JSON {{
    "tables": [], 
    "fields": [],
    "relationships": []
    }}
    """
    return LLM_2

def gen_LLM_3_prompt(user_question, LLM_1_result, LLM_2_result):
    """
    智能体三：SQL语句生成
    根据用户的意图和匹配到的数据库表，生成相应的SQL语句。
    """
    LLM_3 = f"""
    -- 用户问题：{user_question} -- 这里需要插入用户的问题
    -- 识别意图：{LLM_1_result} -- 这里需要插入智能体一的输出结果
    -- 匹配表和字段：{LLM_2_result} -- 这里需要插入智能体二的输出结果
    请按步骤生成SQL：
    1. 确定基础语句结构（SELECT/UPDATE等）
    2. 组装字段列表（显式指定而非使用*）
    3. 构建WHERE条件（注意数据类型匹配）
    4. 处理表连接（JOIN条件）
    5. 添加必要子句（GROUP BY/ORDER BY等）
    生成3个候选SQL后：
    - 对比执行效率
    - 检查NULL值处理
    - 验证结果集是否满足需求
    自我检查：是否存在更优化的索引利用方式？
    最终输出：带注释的SQL语句
    """
    return LLM_3

def gen_LLM_4_prompt(user_question, LLM_1_result, LLM_2_result, LLM_3_result):
    """
    智能体四：SQL语句审核
    根据用户的意图和生成的SQL语句，审核SQL语句的正确性和安全性。
    """
    LLM_4 = f"""
    -- 用户问题：{user_question} -- 这里需要插入用户的问题
    -- 识别意图：{LLM_1_result} -- 这里需要插入智能体一的输出结果
    -- 匹配表和字段：{LLM_2_result} -- 这里需要插入智能体二的输出结果
    -- 生成SQL语句：{LLM_3_result} -- 这里需要插入智能体三的输出结果
    执行完整审核流程：
    【正确性检查】
    1. 语法验证（通过EXPLAIN测试）
    2. 结果验证（是否覆盖所有需求）
    3. 权限验证（执行账户权限）

    【安全性检查】
    1. 注入风险检测（是否存在拼接痕迹）
    2. 敏感操作检查（DELETE/UPDATE是否有WHERE）
    3. 数据暴露检查（是否返回过多字段）

    【优化建议】
    1. 索引使用情况
    2. 潜在性能瓶颈
    3. 可维护性改进



    自我检查：是否需要添加事务控制？
    最终输出格式：JSON {{
    "valid": bool,
    "security_issues": [],
    "optimization_suggestions": [],
    "final_sql": ""
    }}
    final_sql中的SQL语句仅仅为SQL语句的最终版本，
    不需要包含注释和其他信息。
    """
    return LLM_4

if __name__ == "__main__":
    # 示例输入
    user_question = "请查询2023年销售额超过10000的客户信息"
    schema = {
        "tables": ["customers", "orders", "products"],
        "fields": {
            "customers": ["customer_id", "customer_name", "contact_info"],
            "orders": ["order_id", "customer_id", "order_date", "total_amount"],
            "products": ["product_id", "product_name", "price"]
        },
        "relationships": {
            "customers": ["orders.customer_id"],
            "orders": ["products.product_id"]
        }
    }

    # 生成各个智能体的提示
    prompt_1 = gen_LLM_1_prompt(user_question)
    prompt_2 = gen_LLM_2_prompt("意图识别结果", schema)
    prompt_3 = gen_LLM_3_prompt(user_question, "意图识别结果", "表匹配结果")
    prompt_4 = gen_LLM_4_prompt(user_question, "意图识别结果", "表匹配结果", "SQL生成结果")

    print(prompt_1)
    print(prompt_2)
    print(prompt_3)
    print(prompt_4)
    