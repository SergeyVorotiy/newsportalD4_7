from django import forms

from .models import Post, Author

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'heading',
            'text',
        ]

        def form_valid(self, form):
            post = form.save(commit=False)
            # if form.request.


            return super().form_valid(form)


