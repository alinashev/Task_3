class Counter:
    def counting(json_string, start_value, end_value):
        number = 0
        for i in range(start_value, end_value):
            if json_string['questions'][i]['id'] != "":
                number += 1
        return number
