from django.shortcuts import render
from farms import forms

# Create your views here.
def farm_name(request):
    if request.method == 'POST':
        # Getting the forms from the POST request
        farm_form = forms.CreateFarmForm(request.POST)
        phone_form = forms.TelephoneCreateForm(request.POST)
        address_form = forms.AddressCreateForm(request.POST)

        # Checking all the forms for validation
        if farm_form.is_valid and phone_form.is_valid and address_form.is_valid:

            farm = farm_form.save(commit=False)     # before we save into the db
            farm.recorded_by = request.user         # we assigne the user -> this will fail if you are not logged in, try to login with your superuser for example
            farm.save()                             # afterwards, we save the instance

            phone = phone_form.save(commit=False)   # before we save into the db
            phone.farm = farm                       # we assigne the farm instance
            phone.save()                            # afterwards, we save the instance

            address = address_form.save(commit=False) # the same as previous one
            address.farm = farm
            address.save()

    farm_form = forms.CreateFarmForm()
    phone_form = forms.TelephoneCreateForm()
    address_form = forms.AddressCreateForm()
    context = {'farm_form':farm_form, 'phone_form':phone_form, 'address_form':address_form,}
    return render(request, "farms/farm.html", context)
