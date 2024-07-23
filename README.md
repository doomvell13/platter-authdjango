# platter-authdjango

To create SuperUser/Owner
python manage.py createsuperuser

<img width="694" alt="Screenshot 2024-07-22 at 5 51 42 PM" src="https://github.com/user-attachments/assets/d858611f-f45f-4374-b81e-edcff1d1707b">

input your email address & password

## Run Server
python manage.py runserver

## To log in 
http://127.0.0.1:8000/admin/login/
with the Owner email and password

<img width="391" alt="Screenshot 2024-07-22 at 5 52 43 PM" src="https://github.com/user-attachments/assets/8efa2833-6398-4098-abb0-f1ad53829322">


## Access Controls

Group Access
<img width="1088" alt="Screenshot 2024-07-22 at 5 45 24 PM" src="https://github.com/user-attachments/assets/c5ac7da5-471f-48aa-b746-615b3782b9ed">

Store Manager Access
<img width="1377" alt="Screenshot 2024-07-22 at 3 37 35 PM" src="https://github.com/user-attachments/assets/ebdac1a3-167e-4c31-8b22-441ea6b495b6">

<img width="1065" alt="Screenshot 2024-07-23 at 8 50 02 AM" src="https://github.com/user-attachments/assets/b596b68e-1172-43cd-8353-aaddba79d936">

Zonal Manager Access
<img width="1377" alt="Screenshot 2024-07-22 at 3 37 56 PM" src="https://github.com/user-attachments/assets/2edc3679-9f80-48e5-ad37-ceae1031cc81">

<img width="1088" alt="Screenshot 2024-07-22 at 3 41 58 PM" src="https://github.com/user-attachments/assets/943cac69-a4e2-4c98-b153-cae0caec3492">

Branch Location 
<img width="1088" alt="Screenshot 2024-07-22 at 5 47 34 PM" src="https://github.com/user-attachments/assets/4aa94828-397d-4241-8e35-cc42a0640b62">

<img width="1065" alt="Screenshot 2024-07-23 at 9 02 39 AM" src="https://github.com/user-attachments/assets/70030726-1813-46b8-9f87-9341fe1bf64f">

District Office
<img width="1088" alt="Screenshot 2024-07-22 at 5 48 00 PM" src="https://github.com/user-attachments/assets/4df4b46c-cc34-4a44-98f5-8248c9e76fae">

Head Office
<img width="1088" alt="Screenshot 2024-07-22 at 5 48 21 PM" src="https://github.com/user-attachments/assets/69f564f1-5281-4f5e-9cbb-b53c258080cb">


## Bugs to fix
1 - Created owner account need to be done in multi-tenancy approach. Tenant will have it's own class of HeadOffice, DistrictOffice, BranchLocation.
