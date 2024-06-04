# AccuKnox-Project


> First version Deployment to be done on Shahil Khan 
> jun 4 - 2024


### Activating the virtual environment
The virtual environment in created as .venv
activate that by running the following command :
```
source  venv/bin/activate
```

or delete the .env file and recreate again

```
python3 -m venv .env
```
And then activate it again

### Installing dependencies

The requirements.txt file is added to this repo 
run it by running this :

```
pip install -r requirements.txt
```
### Migrations

```
1st Migrate User Model and run
python manage.py makemigrations activity_mapping appointment booking_slot  component consultation consultation_instruction consultation_investigation consultation_medicine consultation_symptom contact_detail doctor_receptionist_mapping entity entity_type fee_structure investigation_master leave_calender medicine_master patient_vital prescription_setting procedure  role saved_note saved_patient specialization specialization_procedure_mapping specialization_workflow_mapping symptom_master template_master test_report user_entity_mapping user_role_mapping user_specialization_procedure_mapping vital_master workflow workflow_component_mapping

```
then Migrate


### Create SuperUser


## Adding Sample Data for Test Purposes

Adding the Specialization and User which will be required to create appointments
```
python3 manage.py load_user               
```
