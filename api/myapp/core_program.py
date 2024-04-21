from aima3S.logic import FolKB, fol_bc_ask, expr

def inference_engine(grades, level, interests, skill1, skill2, preferences, values, jobOutlook):
    

    Kb = FolKB()

    # Rules
    Kb.tell(expr('FavSubject(x , exellent) ==> FavSubject(x , good)'))
    Kb.tell(expr('FavSubject(x , good) ==> FavSubject(x , bad)'))
    Kb.tell(expr('JobOutlook(No) ==> JobOutlook(Yes)'))

    # Queries
    Kb.tell(expr('Decision(major , grades , level , interests , skill1 , skill2 , preferences , values , jobOutlook )'))

    # Business
    Kb.tell(expr('Decision(Business , Economics , Exellent , Entrepreneurship , Marketing , Team_work , Working_alone , Flexibility , Yes )'))
    Kb.tell(expr('Decision(Business , Economics , Exellent , Entrepreneurship , Marketing , Critical_Thinking , Working_alone , Flexibility , Yes )'))
    Kb.tell(expr('Decision(Business , Economics , Exellent , Entrepreneurship , Marketing , Mentorship , Working_alone , Flexibility , Yes )'))
    Kb.tell(expr('Decision(Business , Accounting , Exellent , Entrepreneurship , Marketing , Team_work , Working_alone , Flexibility , Yes )'))
    Kb.tell(expr('Decision(Business , Accounting , Exellent , Entrepreneurship , Marketing , Critical_Thinking , Working_alone , Flexibility , Yes )'))
    Kb.tell(expr('Decision(Business , Accounting , Exellent , Entrepreneurship , Marketing , Mentorship , Working_alone , Flexibility , Yes )'))
    Kb.tell(expr('Decision(Business , Math , Good , Entrepreneurship , Marketing , Team_work , Working_alone , Flexibility , Yes )'))
    Kb.tell(expr('Decision(Business , Math , Good , Entrepreneurship , Marketing , Critical_Thinking , Working_alone , Flexibility , Yes )'))
    Kb.tell(expr('Decision(Business , Math , Good , Entrepreneurship , Marketing , Mentorship , Working_alone , Flexibility , Yes )'))

    # Literature
    Kb.tell(expr('Decision(Literature , English , Exellent , Reading , Writting , Art , Working_alone , Nothing , No )'))
    Kb.tell(expr('Decision(Literature , English , Exellent , Culture , Writting , Art , Working_alone , Nothing , No )'))
    Kb.tell(expr('Decision(Literature , French , Exellent , Reading , Writting , Art , Working_alone , Nothing , No )'))
    Kb.tell(expr('Decision(Literature , French, Exellent , Culture , Writting , Art , Working_alone , Nothing , No )'))
    Kb.tell(expr('Decision(Literature , Arabic , Exellent , Reading , Writting , Art , Working_alone , Nothing , No )'))
    Kb.tell(expr('Decision(Literature , Arabic , Exellent , Culture , Writting , Art , Working_alone , Nothing , No )'))
    Kb.tell(expr('Decision(Literature , Philosophy , Good , Reading , Writting , Art , Working_alone , Nothing , No )'))
    Kb.tell(expr('Decision(Literature , History , Good , Reading , Writting , Art , Working_alone , Nothing , No )'))

    # Law
    Kb.tell(expr('Decision(Law , History , Good , Debate , Public_speaking ,Critical_Thinking, Working_with_ppl , Society_serving , Yes )'))
    Kb.tell(expr('Decision(Law , Ethics , Good , Debate , Public_speaking ,Critical_Thinking, Working_with_ppl , Society_serving , Yes )'))

    # CS
    Kb.tell(expr('Decision(CS, Physics, Good, Electronics, Critical_Thinking, Problem_solving, Working-alone, Flexibility, Yes)'))
    Kb.tell(expr('Decision(CS, Maths, Excellent, Electronics, Critical_Thinking, Problem_solving, Working-alone, Flexibility, Yes)'))
    Kb.tell(expr('Decision(CS, Physics, Good, Programming, Critical_Thinking, Problem_solving, Working-alone, Flexibility, Yes)'))
    Kb.tell(expr('Decision(CS, Maths, Excellent, Programming, Critical_Thinking, Problem_solving, Working-alone, Flexibility, Yes)'))

    # Teaching
    Kb.tell(expr('Decision(Teaching, Physics, Excellent, Mentoring, Expertize, Critical_Thinking, Organizing, Working_with_ppl, Society_serving, Yes)'))
    Kb.tell(expr('Decision(Teaching, Maths, Excellent, Mentoring, Expertize, Critical_Thinking, Organizing, Working_with_ppl, Society_serving, Yes)'))
    Kb.tell(expr('Decision(Teaching, Science, Excellent, Mentoring, Expertize, Critical_Thinking, Organizing, Working_with_ppl, Society_serving, Yes)'))

    # Medicine
    Kb.tell(expr('Decision(Medicine , Chemistry , Exellent , Science , Teamwork , Communication , Working_with_ppl , Society_serving , Yes)'))
    Kb.tell(expr('Decision(Medicine , Chemistry , Exellent , Science , Teamwork , Attention_to_Detail , Working_with_ppl , Society_serving , Yes)'))
    Kb.tell(expr('Decision(Medicine , Chemistry , Exellent , Science , Attention_to_Detail , Communication , Working_with_ppl , Society_serving , Yes)'))

    # Pharmacy
    Kb.tell(expr('Decision(Pharmacy , Chemistry , Exellent , Research , Teamwork , Communication , Working_with_ppl , Flexibility , Yes)'))

    # Psychology
    Kb.tell(expr('Decision(Psychology , Chemistry , Good , Science , Teamwork , Communication , Working_with_ppl , Society_serving , Yes)'))
    Kb.tell(expr('Decision(Psychology , Chemistry , Good , Science , Teamwork , Analytical_Thinking , Working_with_ppl , Society_serving , Yes)'))
    Kb.tell(expr('Decision(Psychology , Chemistry , Good , Science , Teamwork , Analytical_Thinking , Working_with_ppl , Society_serving , Yes)'))

    # Add all the majors
    majors = ['Business', 'Literature', 'Law', 'CS', 'Teaching', 'Medicine', 'Pharmacy', 'Psychology']

    for major in majors:
        result = fol_bc_ask(Kb, expr(f'Decision({major} , {grades} , {level} , {interests} , {skill1} , {skill2} , {preferences} , {values} , {jobOutlook} )'))
        result = list(result)

        if (grades, level, interests, skill1, skill2, preferences, values, jobOutlook) in result:
            rules = Kb.explain(expr(f'Decision({major} , {grades} , {level} , {interests} , {skill1} , {skill2} , {preferences} , {values} , {jobOutlook} )'))
            return f"{major}", rules

    return "We weren't able to find a suitable major for you, but you can always retry", []
