import jutge_api_client as jutge

email = "biel.sevillano@estudiantat.upc.edu"
password = "Billy4AECAM5"

j = jutge.JutgeApiClient()
j.login(email, password)

with open("problems.txt", "r") as f:
    for line in f:
        problem_id = line.strip()
        if problem_id == "CHANGE":
            continue
        statement = j.problems.get_text_statement(problem_id)
        print(f"Problem ID: {problem_id}")
        existing_submissions = j.student.submissions.index_for_problem(problem_id)
        for id, submission in existing_submissions.items():
            print(f"Submission ID: {id}")
            print(submission.state)
            print(submission.veredict)
            
        print("\n" + "="*40 + "\n")