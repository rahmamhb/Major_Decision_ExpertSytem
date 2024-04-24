from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from aima3.logic import FolKB, fol_fc_ask, expr

global kb, agenda 

kb = FolKB()

agenda = []


@csrf_exempt
def form(request):

    # Literature
    kb.tell(expr(f'EnglishExcellent({name}) & Reading({name}) & Writing({name}) & Art({name}) & Working_alone({name}) & Nothing({name}) & No({name}) ==> Literature({name})'))
    kb.tell(expr(f'HistoryGood({name}) & Reading({name}) & Writing({name}) & Art({name}) & Working_alone({name}) & Nothing({name}) & No({name}) ==> Literature({name})'))

    # Law
    kb.tell(expr(f'HistoryGood({name}) & Debate({name}) & Public_speaking({name}) & Critical_Thinking({name}) & Working_with_ppl({name}) & Society_serving({name}) & Yes({name}) ==> Law({name})'))
    kb.tell(expr(f'EthicsGood({name}) & Debate({name}) & Public_speaking({name}) & Critical_Thinking({name}) & Working_with_ppl({name}) & Society_serving({name}) & Yes({name}) ==> Law({name})'))

    # Business
    kb.tell(expr(f'EconomicsExcellent({name}) & Entrepreneurship({name}) & Marketing({name}) & Team_work({name}) & Working_alone({name}) & Flexibility({name}) & Yes({name}) ==> Business({name})'))
    kb.tell(expr(f'EconomicsExcellent({name}) & Entrepreneurship({name}) & Marketing({name}) & Critical_Thinking({name}) & Working_alone({name}) & Flexibility({name}) & Yes({name}) ==> Business({name})'))
    kb.tell(expr(f'EconomicsExcellent({name}) & Entrepreneurship({name}) & Marketing({name}) & Mentorship({name}) & Working_alone({name}) & Flexibility({name}) & Yes({name}) ==> Business({name})'))
    kb.tell(expr(f'AccountingExcellent({name}) & Entrepreneurship({name}) & Marketing({name}) & Team_work({name}) & Working_alone({name}) & Flexibility({name}) & Yes({name}) ==> Business({name})'))
    kb.tell(expr(f'AccountingExcellent({name}) & Entrepreneurship({name}) & Marketing({name}) & Critical_Thinking({name}) & Working_alone({name}) & Flexibility({name}) & Yes({name}) ==> Business({name})'))
    kb.tell(expr(f'AccountingExcellent({name}) & Entrepreneurship({name}) & Marketing({name}) & Mentorship({name}) & Working_alone({name}) & Flexibility({name}) & Yes({name}) ==> Business({name})'))
    kb.tell(expr(f'MathGood({name}) & Entrepreneurship({name}) & Marketing({name}) & Team_work({name}) & Working_alone({name}) & Flexibility({name}) & Yes({name}) ==> Business({name})'))
    kb.tell(expr(f'MathGood({name}) & Entrepreneurship({name}) & Marketing({name}) & Critical_Thinking({name}) & Working_alone({name}) & Flexibility({name}) & Yes({name}) ==> Business({name})'))
    kb.tell(expr(f'MathGood({name}) & Entrepreneurship({name}) & Marketing({name}) & Mentorship({name}) & Working_alone({name}) & Flexibility({name}) & Yes({name}) ==> Business({name})'))

    # Teaching
    kb.tell(expr(f'PhysicsExcellent({name}) & Mentoring({name}) & Expertize({name}) & Critical_Thinking({name}) & Organizing({name}) & Working_with_ppl({name}) & Society_serving({name}) & Yes({name}) ==> Teaching({name})'))
    kb.tell(expr(f'MathsExcellent({name}) & Mentoring({name}) & Expertize({name}) & Critical_Thinking({name}) & Organizing({name}) & Working_with_ppl({name}) & Society_serving({name}) & Yes({name}) ==> Teaching({name})'))
    kb.tell(expr(f'ScienceExcellent({name}) & Mentoring({name}) & Expertize({name}) & Critical_Thinking({name}) & Organizing({name}) & Working_with_ppl({name}) & Society_serving({name}) & Yes({name}) ==> Teaching({name})'))

    # Medicine
    kb.tell(expr(f'ChemistryExcellent({name}) & Science({name}) & Teamwork({name}) & Communication({name}) & Working_with_ppl({name}) & Society_serving({name}) & Yes({name}) ==> Medicine({name})'))
    kb.tell(expr(f'ChemistryExcellent({name}) & Science({name}) & Teamwork({name}) & Attention_to_Detail({name}) & Working_with_ppl({name}) & Society_serving({name}) & Yes({name}) ==> Medicine({name})'))
    kb.tell(expr(f'ChemistryExcellent({name}) & Science({name}) & Attention_to_Detail({name}) & Communication({name}) & Working_with_ppl({name}) & Society_serving({name}) & Yes({name}) ==> Medicine({name})'))

    # Pharmacy
    kb.tell(expr(f'ChemistryExcellent({name}) & Research({name}) & Teamwork({name}) & Communication({name}) & Working_with_ppl({name}) & Flexibility({name}) & Yes({name}) ==> Pharmacy({name})'))

    # Psychology
    kb.tell(expr(f'ChemistryGood({name}) & Science({name}) & Teamwork({name}) & Communication({name}) & Working_with_ppl({name}) & Society_serving({name}) & Yes({name}) ==> Psychology({name})'))
    kb.tell(expr(f'ChemistryGood({name}) & Science({name}) & Teamwork({name}) & Analytical_Thinking({name}) & Working_with_ppl({name}) & Society_serving({name}) & Yes({name}) ==> Psychology({name})'))

    kb.tell(expr(f'PhysicsGood(name) & Electronics(name) & Critical_Thinking(name) & Problem_solving(name) & Working_alone(name) & Flexibility(name) & Yes(name) ==> CS(name)'))
    kb.tell(expr(f'MathExcellent(name) & PhysicsGood(name) & Electronics(name) & Critical_Thinking(name) & Problem_solving(name) & Working_alone(name) & Flexibility(name) & Yes(name) ==> CS(name)'))
    kb.tell(expr(f'MathGood(name) & PhysicsGood(name) & Electronics(name) & Critical_Thinking(name) & Problem_solving(name) & Working_alone(name) & Flexibility(name) & Yes(name) ==> CS(name)'))
    kb.tell(expr(f'PhysicsGood(name) & Programming(name) & Critical_Thinking(name) & Problem_solving(name) & Working_alone(name) & Flexibility(name) & Yes(name) ==> CS(name)'))


    if request.method == 'GET':
        data = request.GET
        print(data)
        selected_option = data.get('selectOption')
        selected_skill = data.get('selectSkill')

        selected_preference = data.get('personalityType')
        selected_outlook = data.get('yesNoSelection')

        marks = {
            'history': int(data.get('history', 0)),
            'ethics': int(data.get('ethics', 0)),
            'arabic': int(data.get('arabic', 0)),
            'philosophy': int(data.get('philosophy', 0)),
            'french': int(data.get('french', 0)),
            'english': int(data.get('english', 0)),
            'economics': int(data.get('economics', 0)),
            'accounting': int(data.get('accounting', 0)),
            'math': int(data.get('math', 0)),
            'chemistry': int(data.get('chemistry', 0)),
            'biology': int(data.get('biology', 0)),
            'psychology': int(data.get('psychology', 0)),
            'statistics': int(data.get('statistics', 0))
        }

        username = 'Bassmala'

        # Define variables
        name = expr(username)

        # This part will add the selected options and skills of the user
        agenda.append(expr(f'EnglishExcellent({name})' if selected_option == 'option1' else ''))
        agenda.append(expr(f'Art({name})' if selected_option == 'option2' else ''))
        agenda.append(expr(f'Entrepreneurship({name})' if selected_option == 'option3' else ''))
        agenda.append(expr(f'Mentoring({name})' if selected_option == 'option4' else ''))
        agenda.append(expr(f'Teaching({name})' if selected_option == 'option5' else ''))
        agenda.append(expr(f'Expertize({name})' if selected_option == 'option6' else ''))
        agenda.append(expr(f'Psychology({name})' if selected_option == 'option7' else ''))
        agenda.append(expr(f'Science({name})' if selected_option == 'option8' else ''))
        agenda.append(expr(f'Research({name})' if selected_option == 'option9' else ''))
        agenda.append(expr(f'Culture({name})' if selected_option == 'option10' else ''))
        agenda.append(expr(f'Debate({name})' if selected_option == 'option11' else ''))

        agenda.append(expr(f'Public_speaking({name})' if selected_skill == 'skill1' else ''))
        agenda.append(expr(f'Critical_Thinking({name})' if selected_skill == 'skill2' else ''))
        agenda.append(expr(f'Writing({name})' if selected_skill == 'skill3' else ''))
        agenda.append(expr(f'Problem_solving({name})' if selected_skill == 'skill4' else ''))

        agenda.append(expr(f'{selected_preference}({name})'))

        agenda.append(expr(f'Yes({name})' if selected_outlook == 'yes' else ''))
        agenda.append(expr(f'No({name})' if selected_outlook == 'no' else ''))

        # Define a function to set the expression according to the grade
        def grade_expression(subject, grade):
            if 0 <= grade <= 10:
                return f'{subject}Bad({name})'
            elif 10 < grade <= 15:
                return f'{subject}Good({name})'
            elif 15 < grade <= 20:
                return f'{subject}Excellent({name})'

        for subject, mark in marks.items():
            agenda.append(expr(grade_expression(subject, mark)))
        
        formresult(agenda)

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def formresult(agenda):
    name = 'Bassmala'
    memory = {}

    seen = set()  

    while agenda:
        p = agenda.pop(0)
        if p in seen:
            continue  
        seen.add(p)
        if fol_fc_ask(kb, p):
            memory[p] = True
        else:
            memory[p] = False
            
        # Check if new rules can be activated
        if memory.get(expr(f'EnglishExcellent({name})'), False) and memory.get(expr(f'Art({name})'), False) and \
           memory.get(expr(f'Entrepreneurship({name})'), False) and memory.get(expr(f'Mentoring({name})'), False) and \
           memory.get(expr(f'Teaching({name})'), False) and memory.get(expr(f'Expertize({name})'), False) and \
           memory.get(expr(f'Psychology({name})'), False) and memory.get(expr(f'Science({name})'), False) and \
           memory.get(expr(f'Research({name})'), False) and memory.get(expr(f'Culture({name})'), False) and \
           memory.get(expr(f'Debate({name})'), False):
           agenda.append(expr(f'Business({name})'))

        if memory.get(expr(f'Public_speaking({name})'), False) and memory.get(expr(f'Critical_Thinking({name})'), False) and \
           memory.get(expr(f'Writing({name})'), False) and memory.get(expr(f'Problem_solving({name})'), False):
           agenda.append(expr(f'CS({name})'))

        if memory.get(expr(f'EnglishExcellent({name})'), False) and memory.get(expr(f'Reading({name})'), False) and \
           memory.get(expr(f'Writing({name})'), False) and memory.get(expr(f'Art({name})'), False) and \
           memory.get(expr(f'Working_alone({name})'), False) and memory.get(expr(f'Nothing({name})'), False) and \
           memory.get(expr(f'No({name})'), False):
           agenda.append(expr(f'Literature({name})'))

        if memory.get(expr(f'HistoryGood({name})'), False) and memory.get(expr(f'Reading({name})'), False) and \
           memory.get(expr(f'Writing({name})'), False) and memory.get(expr(f'Art({name})'), False) and \
           memory.get(expr(f'Working_alone({name})'), False) and memory.get(expr(f'Nothing({name})'), False) and \
           memory.get(expr(f'No({name})'), False):
           agenda.append(expr(f'Literature({name})'))

        if memory.get(expr(f'HistoryGood({name})'), False) and memory.get(expr(f'Debate({name})'), False) and \
           memory.get(expr(f'Public_speaking({name})'), False) and memory.get(expr(f'Critical_Thinking({name})'), False) and \
           memory.get(expr(f'Working_with_ppl({name})'), False) and memory.get(expr(f'Society_serving({name})'), False) and \
           memory.get(expr(f'Yes({name})'), False):
           agenda.append(expr(f'Law({name})'))

        if memory.get(expr(f'EthicsGood({name})'), False) and memory.get(expr(f'Debate({name})'), False) and \
           memory.get(expr(f'Public_speaking({name})'), False) and memory.get(expr(f'Critical_Thinking({name})'), False) and \
           memory.get(expr(f'Working_with_ppl({name})'), False) and memory.get(expr(f'Society_serving({name})'), False) and \
           memory.get(expr(f'Yes({name})'), False):
           agenda.append(expr(f'Law({name})'))

        if memory.get(expr(f'PhysicsExcellent({name})'), False) and memory.get(expr(f'Mentoring({name})'), False) and \
        memory.get(expr(f'Expertize({name})'), False) and memory.get(expr(f'Critical_Thinking({name})'), False) and \
        memory.get(expr(f'Organizing({name})'), False) and memory.get(expr(f'Working_with_ppl({name})'), False) and \
        memory.get(expr(f'Society_serving({name})'), False) and memory.get(expr(f'Yes({name})'), False):
           agenda.append(expr(f'Teaching({name})'))

        if memory.get(expr(f'MathsExcellent({name})'), False) and memory.get(expr(f'Mentoring({name})'), False) and \
        memory.get(expr(f'Expertize({name})'), False) and memory.get(expr(f'Critical_Thinking({name})'), False) and \
        memory.get(expr(f'Organizing({name})'), False) and memory.get(expr(f'Working_with_ppl({name})'), False) and \
        memory.get(expr(f'Society_serving({name})'), False) and memory.get(expr(f'Yes({name})'), False):
           agenda.append(expr(f'Teaching({name})'))

        if memory.get(expr(f'ScienceExcellent({name})'), False) and memory.get(expr(f'Mentoring({name})'), False) and \
        memory.get(expr(f'Expertize({name})'), False) and memory.get(expr(f'Critical_Thinking({name})'), False) and \
        memory.get(expr(f'Organizing({name})'), False) and memory.get(expr(f'Working_with_ppl({name})'), False) and \
        memory.get(expr(f'Society_serving({name})'), False) and memory.get(expr(f'Yes({name})'), False):
           agenda.append(expr(f'Teaching({name})'))

        if memory.get(expr(f'ChemistryExcellent({name})'), False) and memory.get(expr(f'Science({name})'), False) and \
        memory.get(expr(f'Teamwork({name})'), False) and memory.get(expr(f'Communication({name})'), False) and \
        memory.get(expr(f'Working_with_ppl({name})'), False) and memory.get(expr(f'Society_serving({name})'), False) and \
        memory.get(expr(f'Yes({name})'), False):
           agenda.append(expr(f'Medicine({name})'))

        if memory.get(expr(f'ChemistryExcellent({name})'), False) and memory.get(expr(f'Science({name})'), False) and \
        memory.get(expr(f'Teamwork({name})'), False) and memory.get(expr(f'Attention_to_Detail({name})'), False) and \
        memory.get(expr(f'Working_with_ppl({name})'), False) and memory.get(expr(f'Society_serving({name})'), False) and \
        memory.get(expr(f'Yes({name})'), False):
           agenda.append(expr(f'Medicine({name})'))

        if memory.get(expr(f'ChemistryExcellent({name})'), False) and memory.get(expr(f'Science({name})'), False) and \
        memory.get(expr(f'Attention_to_Detail({name})'), False) and memory.get(expr(f'Communication({name})'), False) and \
        memory.get(expr(f'Working_with_ppl({name})'), False) and memory.get(expr(f'Society_serving({name})'), False) and \
        memory.get(expr(f'Yes({name})'), False):
           agenda.append(expr(f'Medicine({name})'))

        if memory.get(expr(f'ChemistryExcellent({name})'), False) and memory.get(expr(f'Research({name})'), False) and \
        memory.get(expr(f'Teamwork({name})'), False) and memory.get(expr(f'Communication({name})'), False) and \
        memory.get(expr(f'Working_with_ppl({name})'), False) and memory.get(expr(f'Flexibility({name})'), False) and \
        memory.get(expr(f'Yes({name})'), False):
           agenda.append(expr(f'Pharmacy({name})'))

        if memory.get(expr(f'ChemistryGood({name})'), False) and memory.get(expr(f'Science({name})'), False) and \
        memory.get(expr(f'Teamwork({name})'), False) and memory.get(expr(f'Communication({name})'), False) and \
        memory.get(expr(f'Working_with_ppl({name})'), False) and memory.get(expr(f'Society_serving({name})'), False) and \
        memory.get(expr(f'Yes({name})'), False):
           agenda.append(expr(f'Psychology({name})'))

        if memory.get(expr(f'ChemistryGood({name})'), False) and memory.get(expr(f'Science({name})'), False) and \
        memory.get(expr(f'Teamwork({name})'), False) and memory.get(expr(f'Analytical_Thinking({name})'), False) and \
        memory.get(expr(f'Working_with_ppl({name})'), False) and memory.get(expr(f'Society_serving({name})'), False) and \
        memory.get(expr(f'Yes({name})'), False):
           agenda.append(expr(f'Psychology({name})'))

        if memory.get(expr(f'PhysicsGood({name})'), False) and memory.get(expr(f'Electronics({name})'), False) and \
        memory.get(expr(f'Critical_Thinking({name})'), False) and memory.get(expr(f'Problem_solving({name})'), False) and \
        memory.get(expr(f'Working_alone({name})'), False) and memory.get(expr(f'Flexibility({name})'), False) and \
        memory.get(expr(f'Yes({name})'), False):
            agenda.append(expr(f'CS({name})'))

        if memory.get(expr(f'MathExcellent({name})'), False) and memory.get(expr(f'PhysicsGood({name})'), False) and \
        memory.get(expr(f'Electronics({name})'), False) and memory.get(expr(f'Critical_Thinking({name})'), False) and \
        memory.get(expr(f'Problem_solving({name})'), False) and memory.get(expr(f'Working_alone({name})'), False) and \
        memory.get(expr(f'Flexibility({name})'), False) and memory.get(expr(f'Yes({name})'), False):
             agenda.append(expr(f'CS({name})'))
 
        if memory.get(expr(f'MathGood({name})'), False) and memory.get(expr(f'PhysicsGood({name})'), False) and \
        memory.get(expr(f'Electronics({name})'), False) and memory.get(expr(f'Critical_Thinking({name})'), False) and \
        memory.get(expr(f'Problem_solving({name})'), False) and memory.get(expr(f'Working_alone({name})'), False) and \
        memory.get(expr(f'Flexibility({name})'), False) and memory.get(expr(f'Yes({name})'), False):
            agenda.append(expr(f'CS({name})'))

        if memory.get(expr(f'PhysicsGood({name})'), False) and memory.get(expr(f'Programming({name})'), False) and \
        memory.get(expr(f'Critical_Thinking({name})'), False) and memory.get(expr(f'Problem_solving({name})'), False) and \
        memory.get(expr(f'Working_alone({name})'), False) and memory.get(expr(f'Flexibility({name})'), False) and \
        memory.get(expr(f'Yes({name})'), False):
            agenda.append(expr(f'CS({name})'))

    
    print('Final result:')
    for p, value in memory.items():
        if value:
            print(f'{p}')
    return value


@csrf_exempt
def formresults(request):
    if request.method == 'POST':
        if formresult:
            result_text = str(formresult[0])[7:]
            return JsonResponse({'result': result_text})
        else:
            return JsonResponse({'result': "Sorry, the system cannot make a decision based on the given information."})
    else:
        return JsonResponse({'error': 'Invalid request method'})


