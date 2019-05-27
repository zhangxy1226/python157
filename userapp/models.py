from django.db import models


class AdrssInfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recipient = models.CharField(max_length=20, blank=True, null=True)
    adress = models.CharField(max_length=80, blank=True, null=True)
    zip_code = models.BigIntegerField(blank=True, null=True)
    tel = models.BigIntegerField(db_column='TEL', blank=True, null=True)  # Field name made lowercase.
    phone = models.BigIntegerField(blank=True, null=True)
    pid = models.ForeignKey('User', models.DO_NOTHING, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adrss_info'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BookClassT(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_class_t'


class BooksT(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_name = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    press = models.CharField(max_length=30, blank=True, null=True)
    press_date = models.DateField(blank=True, null=True)
    edition = models.BigIntegerField(blank=True, null=True)
    printing_time = models.DateField(blank=True, null=True)
    impression = models.BigIntegerField(blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    words = models.BigIntegerField(blank=True, null=True)
    pages = models.BigIntegerField(blank=True, null=True)
    format = models.CharField(max_length=20, blank=True, null=True)
    paper = models.CharField(max_length=20, blank=True, null=True)
    packing = models.CharField(max_length=20, blank=True, null=True)
    dd_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    save = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pid = models.ForeignKey(BookClassT, models.DO_NOTHING, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books_t'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OrderItem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    book_name = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    count_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    my_or = models.IntegerField(blank=True, null=True)
    pid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='pid', blank=True, null=True)
    book_pid = models.ForeignKey(BooksT, models.DO_NOTHING, db_column='book_pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item'


class Orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    or_num = models.IntegerField(blank=True, null=True)
    recipient = models.CharField(max_length=30, blank=True, null=True)
    adress = models.CharField(max_length=50, blank=True, null=True)
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    aid = models.ForeignKey(AdrssInfo, models.DO_NOTHING, db_column='aid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    pwd = models.CharField(max_length=30, blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    c_time = models.CharField(max_length=255, blank=True, null=True)
    has_confirm = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

