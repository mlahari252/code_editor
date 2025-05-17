import subprocess
from django.shortcuts import render

def code_editor(request):
    output = ''
    input_data = ''
    code = ''

    if request.method == 'POST':
        code = request.POST.get('code')
        input_data = request.POST.get('input_data', '')

        try:
            # Save code to a temporary file
            with open("temp_code.py", "w") as f:
                f.write(code)

            # Run the code using subprocess
            result = subprocess.run(
                ['python', 'temp_code.py'],
                input=input_data.encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5  # seconds
            )
            output = result.stdout.decode() + result.stderr.decode()

        except Exception as e:
            output = str(e)

    return render(request, 'editor.html', {'code': code, 'input_data': input_data, 'output': output})


 




