from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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


class Course(models.Model):
    courseid = models.CharField(db_column='CourseID', primary_key=True, max_length=6)  # Field name made lowercase.
    course_name = models.CharField(db_column='Course Name', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit = models.FloatField(db_column='Credit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course'


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


class Offeredcourse(models.Model):
    offered_course_id = models.ForeignKey(Course, models.DO_NOTHING, db_column='Offered Course ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    teachers_code = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='Teachers Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'offeredcourse'


class Student(models.Model):
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    registrationnumber = models.CharField(db_column='RegistrationNumber', primary_key=True, max_length=10)  # Field name made lowercase.
    session = models.CharField(db_column='Session', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.ForeignKey('Users', models.DO_NOTHING, db_column='Username', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'


class Task(models.Model):
    taskid = models.CharField(db_column='TaskID', primary_key=True, max_length=50)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='Start Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    deadline = models.DateTimeField(db_column='Deadline', blank=True, null=True)  # Field name made lowercase.
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='CourseID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task'


class TaskTeam(models.Model):
    taskid = models.ForeignKey(Task, models.DO_NOTHING, db_column='TaskID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.ForeignKey('Team', models.DO_NOTHING, db_column='TeamID', blank=True, null=True)  # Field name made lowercase.
    due_date = models.DateTimeField(db_column='Due Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    files = models.CharField(db_column='Files', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task-team'


class Teacher(models.Model):
    first_name = models.CharField(db_column='First Name', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.CharField(db_column='Last Name', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    designation = models.CharField(db_column='Designation', max_length=6, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=3, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=12, blank=True, null=True)  # Field name made lowercase.
    username = models.ForeignKey('Users', models.DO_NOTHING, db_column='Username', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teacher'


class Team(models.Model):
    teamid = models.CharField(db_column='TeamID', primary_key=True, max_length=10)  # Field name made lowercase.
    team_name = models.CharField(db_column='Team Name', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    course_id = models.ForeignKey(Offeredcourse, models.DO_NOTHING, db_column='Course ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'team'


class TeamStudent(models.Model):
    team_id = models.ForeignKey(Team, models.DO_NOTHING, db_column='Team ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    registrationnumber = models.ForeignKey(Student, models.DO_NOTHING, db_column='RegistrationNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'team_student'


class Users(models.Model):
    username = models.CharField(db_column='Username', primary_key=True, max_length=50)  # Field name made lowercase.
    pasword = models.CharField(db_column='Pasword', max_length=50)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'