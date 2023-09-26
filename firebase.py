import firebase_admin
from firebase_admin import firestore, credentials

cred = credentials.Certificate("key.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client()


def get_apps():
    apps_ref = db.collection("october")
    apps = apps_ref.stream()

    for app in apps:
        print(f"{app.id} => {app.to_dict()}")


def get_app(app_id):
    app_ref = db.collection("october").document(app_id)
    app = app_ref.get()

    if app.exists:
        return app.to_dict()
    else:
        print("No such app!")


if __name__ == "__main__":
    get_apps()
