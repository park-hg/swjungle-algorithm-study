def solution(id_list, report, k):
    answer = []
    report_count_dict = {}
    report_user_id_dict = {}
    report_mail_dict = {}
    
    for id in id_list:
        report_count_dict[id] = 0
        report_user_id_dict[id] = []
        report_mail_dict[id] = 0

    report_set = set(report)

    for re in list(report_set):
        user_id, report_user_id = re.rstrip().split()
        report_count_dict[report_user_id] += 1
        report_user_id_dict[report_user_id].append(user_id)

    for key, value in report_user_id_dict.items():
        if report_count_dict[key] >= k:
            for user_id in value:
                report_mail_dict[user_id] += 1
                
    for id in id_list:
        answer.append(report_mail_dict[id])
        
    return answer
