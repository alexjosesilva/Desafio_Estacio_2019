BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "authweb_usuario" (
	"user_ptr_id"	integer NOT NULL,
	"matricula"	varchar(14) NOT NULL,
	"categoria"	varchar(255) NOT NULL,
	"timezone"	varchar(50) NOT NULL,
	FOREIGN KEY("user_ptr_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("user_ptr_id")
);
CREATE TABLE IF NOT EXISTS "authweb_foo" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(150) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"first_name"	varchar(30) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"last_name"	varchar(150) NOT NULL
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag">=0),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL
);
INSERT INTO "django_session" VALUES ('l9weerdbu9m1fxgzeq95vnyhyqdu1wpz','NjI5YTBhMjA0OGEwZGI3OGI1NThjMDk3ZmJlNDVlNzg0MTBiMzlhYTp7fQ==','2019-10-31 04:41:08.858119'),
 ('nv83f9c8g701podo02h9gz68f0qgrodd','NDk4MjFiMDY3NDczMDFkNzg4MGE2Y2M0NmJkOTJlMGQ0OTE1MDllMjp7Il9hdXRoX3VzZXJfaWQiOiI2IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkODM0M2NmNDUwYzFjNjEwNjM5ZDhlNGRhNjY2Y2ZhMTQ3Mzc1YTc2In0=','2019-10-31 14:55:14.694668');
INSERT INTO "authweb_usuario" VALUES (1,'14014001','professor','America/Recife'),
 (2,'14014002','professor','America/Recife'),
 (3,'14014003','professor','America/Recife'),
 (4,'16016001','laboratorista','America/Recife'),
 (5,'16016002','laboratorista','America/Recife'),
 (6,'17017001','admin','America/Recife');
INSERT INTO "auth_user" VALUES (1,'123456','2019-10-17 14:06:33.516097',0,'14014001','','professorA@estacio.br',0,1,'2019-10-17 03:13:57.368711',''),
 (2,'123456','2019-10-17 14:08:59.202822',0,'14014002','','professorB@estacio.br',0,1,'2019-10-17 14:08:45.729597',''),
 (3,'123456',NULL,0,'14014003','','professorC@estacio.br',0,1,'2019-10-17 14:09:16.755031',''),
 (4,'123456','2019-10-17 14:12:37.892672',0,'16016001','','laboratoristaA@estacio.br',0,1,'2019-10-17 14:12:27.836699',''),
 (5,'123456',NULL,0,'16016002','','laboratoristaB@estacio.br',0,1,'2019-10-17 14:13:18.061925',''),
 (6,'123456','2019-10-17 14:55:14.589617',0,'17017001','','adm@estacio.br',0,1,'2019-10-17 14:19:46.609611','');
INSERT INTO "auth_permission" VALUES (1,1,'add_logentry','Can add log entry'),
 (2,1,'change_logentry','Can change log entry'),
 (3,1,'delete_logentry','Can delete log entry'),
 (4,1,'view_logentry','Can view log entry'),
 (5,2,'add_permission','Can add permission'),
 (6,2,'change_permission','Can change permission'),
 (7,2,'delete_permission','Can delete permission'),
 (8,2,'view_permission','Can view permission'),
 (9,3,'add_group','Can add group'),
 (10,3,'change_group','Can change group'),
 (11,3,'delete_group','Can delete group'),
 (12,3,'view_group','Can view group'),
 (13,4,'add_user','Can add user'),
 (14,4,'change_user','Can change user'),
 (15,4,'delete_user','Can delete user'),
 (16,4,'view_user','Can view user'),
 (17,5,'add_contenttype','Can add content type'),
 (18,5,'change_contenttype','Can change content type'),
 (19,5,'delete_contenttype','Can delete content type'),
 (20,5,'view_contenttype','Can view content type'),
 (21,6,'add_session','Can add session'),
 (22,6,'change_session','Can change session'),
 (23,6,'delete_session','Can delete session'),
 (24,6,'view_session','Can view session'),
 (25,7,'add_foo','Can add foo'),
 (26,7,'change_foo','Can change foo'),
 (27,7,'delete_foo','Can delete foo'),
 (28,7,'view_foo','Can view foo'),
 (29,8,'add_usuario','Can add user'),
 (30,8,'change_usuario','Can change user'),
 (31,8,'delete_usuario','Can delete user'),
 (32,8,'view_usuario','Can view user');
INSERT INTO "django_content_type" VALUES (1,'admin','logentry'),
 (2,'auth','permission'),
 (3,'auth','group'),
 (4,'auth','user'),
 (5,'contenttypes','contenttype'),
 (6,'sessions','session'),
 (7,'authweb','foo'),
 (8,'authweb','usuario');
INSERT INTO "auth_user_user_permissions" VALUES (1,1,28),
 (2,1,25),
 (3,2,28),
 (4,2,25),
 (5,3,28),
 (6,3,25),
 (7,4,28),
 (8,4,25),
 (9,5,28),
 (10,5,25),
 (11,6,28),
 (12,6,25),
 (13,6,32),
 (14,6,30),
 (15,6,29),
 (16,6,31);
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2019-10-17 03:10:50.574023'),
 (2,'auth','0001_initial','2019-10-17 03:10:50.748015'),
 (3,'admin','0001_initial','2019-10-17 03:10:50.865008'),
 (4,'admin','0002_logentry_remove_auto_add','2019-10-17 03:10:51'),
 (5,'admin','0003_logentry_add_action_flag_choices','2019-10-17 03:10:51.123990'),
 (6,'contenttypes','0002_remove_content_type_name','2019-10-17 03:10:51.272980'),
 (7,'auth','0002_alter_permission_name_max_length','2019-10-17 03:10:51.400976'),
 (8,'auth','0003_alter_user_email_max_length','2019-10-17 03:10:51.536019'),
 (9,'auth','0004_alter_user_username_opts','2019-10-17 03:10:51.675959'),
 (10,'auth','0005_alter_user_last_login_null','2019-10-17 03:10:51.798951'),
 (11,'auth','0006_require_contenttypes_0002','2019-10-17 03:10:51.916946'),
 (12,'auth','0007_alter_validators_add_error_messages','2019-10-17 03:10:52.058936'),
 (13,'auth','0008_alter_user_username_max_length','2019-10-17 03:10:52.199948'),
 (14,'auth','0009_alter_user_last_name_max_length','2019-10-17 03:10:52.321918'),
 (15,'auth','0010_alter_group_name_max_length','2019-10-17 03:10:52.451913'),
 (16,'auth','0011_update_proxy_permissions','2019-10-17 03:10:52.557960'),
 (17,'authweb','0001_initial','2019-10-17 03:10:52.684898'),
 (18,'sessions','0001_initial','2019-10-17 03:10:52.806889');
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
COMMIT;
