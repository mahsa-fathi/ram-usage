def jsonify_ram_results(fetched_results):
    json_result = []
    for item in fetched_results:
        json_result.append(
            {
                "TIME": item[0],
                "TOTAL": item[1],
                "FREE": item[2],
                "USED": item[3]
            }
        )
    return json_result
