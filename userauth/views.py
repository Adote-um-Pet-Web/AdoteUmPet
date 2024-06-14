from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, UpdateView
from django.views.generic.edit import CreateView

from .forms import UserProfileImageUpdateForm, UserRegisterForm, UserUpdateForm
from .models import User


class SignUpView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "sign-up.html"
    success_url = reverse_lazy("pets:index")

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get("username")
        messages.success(
            self.request, f"Hello {username}, your account was created successfully."
        )
        new_user = authenticate(
            username=form.cleaned_data["email"],
            password=form.cleaned_data["password1"],
        )

        login(self.request, new_user)

        if form.cleaned_data.get("image_user_profile"):
            user.image = form.cleaned_data["image_user_profile"]
            user.save()

        return redirect("pets:index")


class UserProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    context_object_name = "user"
    template_name = "userDelete.html"
    success_url = reverse_lazy("userauths:sign-in")

    def get_object(self, queryset=None):
        return self.request.user


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "userUpdate.html"
    context_object_name = "user"
    success_url = reverse_lazy("pets:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["image_form"] = UserProfileImageUpdateForm(instance=self.request.user)
        context["current_user"] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        image_form = UserProfileImageUpdateForm(
            request.POST, request.FILES, instance=self.request.user
        )

        if "image_user_profile" in request.FILES:
            if image_form.is_valid():
                image_form.save()
                messages.success(
                    request, "Your profile picture was updated successfully."
                )
            else:
                messages.error(
                    request, "There was an error updating your profile picture."
                )
        elif form.is_valid():
            form.save()
            messages.success(request, "Your profile was updated successfully.")
        else:
            return self.form_invalid(form)

        return redirect(self.success_url)


class PageConfigUser(LoginRequiredMixin, ListView):
    model = User
    fields = ["username", "email", "phone_number", "image_user_profile"]
    success_url = reverse_lazy("pets:index")
    template_name = "userConfig.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context["current_user"] = current_user
        context["user_update_url"] = reverse_lazy(
            "user-update", kwargs={"pk": current_user.pk}
        )
        return context


class LoginView(CreateView):
    template_name = "sign-in.html"

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in.")
                return redirect("pets:index")
            else:
                messages.warning(request, "Username or password does not exist.")
                return redirect("userauths:sign-in")
        except User.DoesNotExist:
            messages.warning(request, "User does not exist.")

        return render(request, self.template_name)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "You are already logged in.")
            return redirect("pets:index")
        return render(request, self.template_name)


class LogoutView(CreateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect("userauths:sign-in")
