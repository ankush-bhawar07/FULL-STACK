# Access the nested key increment from the following dictionary

emp_dict = {
    "company": {
        "employee": {
            "name": "Jess",
            "payable": {
                "salary": 9000,
                "increment": 12
            }
        }
    }
}
print(emp_dict['company']['employee']['payable']['increment'])