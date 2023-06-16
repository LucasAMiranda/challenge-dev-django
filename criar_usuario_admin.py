import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emprestimo.settings")
django.setup()

from django.contrib.auth.models import User

def criar_usuario_admin():
    # Crie um novo usuário administrador
    User.objects.create_superuser('admin', 'admin@gmail.com', 'admin123')
    print('Usuário administrador criado com sucesso!')

if __name__ == '__main__':
    criar_usuario_admin()
