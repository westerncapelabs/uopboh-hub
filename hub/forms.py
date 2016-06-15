from django import forms


class QuestionForm(forms.Form):
    active = forms.BooleanField(required=False)
    question = forms.CharField(widget=forms.TextInput)
    answer_1_value = forms.CharField(widget=forms.TextInput)
    answer_1_text = forms.CharField(widget=forms.TextInput)
    answer_1_correct = forms.BooleanField(required=False)
    answer_2_value = forms.CharField(widget=forms.TextInput)
    answer_2_text = forms.CharField(widget=forms.TextInput)
    answer_2_correct = forms.BooleanField(required=False)
    answer_3_value = forms.CharField(widget=forms.TextInput, required=False)
    answer_3_text = forms.CharField(widget=forms.TextInput, required=False)
    answer_3_correct = forms.BooleanField(required=False)
    answer_4_value = forms.CharField(widget=forms.TextInput, required=False)
    answer_4_text = forms.CharField(widget=forms.TextInput, required=False)
    answer_4_correct = forms.BooleanField(required=False)
    answer_5_value = forms.CharField(widget=forms.TextInput, required=False)
    answer_5_text = forms.CharField(widget=forms.TextInput, required=False)
    answer_5_correct = forms.BooleanField(required=False)
    response_correct = forms.CharField(widget=forms.TextInput)
    response_incorrect = forms.CharField(widget=forms.TextInput)


class QuizForm(forms.Form):
    active = forms.BooleanField(required=False)
    description = forms.CharField(widget=forms.TextInput)


class QuizAddQuestionsForm(forms.Form):
    questions = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
    )
