from django.http import JsonResponse
from aima3.logic import *
from aima3.utils import *

Kb = FolKB()

def form1(request):
    if request.method == 'POST':
        data = request.POST
        selected_option = data.get('selectOption')
        selected_skill = data.get('selectSkill')
        user_name = data.get('name')

        # Define variables
        name = expr(user_name)

        # This part will add the selected options and skills of the user
        agenda = []
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

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def form2(request):
    if request.method == 'POST':
        data = request.POST
        selected_grade = data.get('selectGrade')
        selected_level = data.get('selectLevel')
        
        name = request.session.get('name')

        # Define a function to set the expression according to the grade
        def grade_expression(subject, grade):
            if 0 <= grade <= 10:
                return f'{subject}Bad({name})'
            elif 10 < grade <= 15:
                return f'{subject}Good({name})'
            elif 15 < grade <= 20:
                return f'{subject}Excellent({name})'

        agenda.append(expr(f'{subject}Good({name})' if  else ''))
        agenda.append(expr(f'{subject}Excellent({name})' if  else ''))

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def form3(request):
    if request.method == 'POST':
        data = request.POST
        selected_preference = data.get('selectPreference')
        selected_value = data.get('selectValue')
        selected_outlook = data.get('selectOutlook')

        agenda = request.session.get('agenda', [])
        name = request.session.get('name')

        agenda.append(expr(f'Team_work({name})' if selected_preference == 'preference1' else ''))
        agenda.append(expr(f'Working_alone({name})' if selected_preference == 'preference2' else ''))

        agenda.append(expr(f'Nothing({name})' if selected_value == 'value1' else ''))
        agenda.append(expr(f'Flexibility({name})' if selected_value == 'value2' else ''))

        agenda.append(expr(f'Yes({name})' if selected_outlook == 'outlook1' else ''))
        agenda.append(expr(f'No({name})' if selected_outlook == 'outlook2' else ''))

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

memory = {}

seen = set()  # Keep track of the conditions already processed
        
while agenda:
            p = agenda.pop(0)
            if p in seen:
            
                continue  # Skip the condition if it has already been processed
            seen.add(p)
            if fol_fc_ask(Kb, p):
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


