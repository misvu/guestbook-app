drop table if exists user;
create table user (
	USERNAME TEXT PRIMARY KEY,
	NAME TEXT not null,
	CITY TEXT not null,
	PASSWORD TEXT NOT NULL
);

drop table if exists comment;
create table comment (
	COMMENTID INTEGER PRIMARY KEY,
	USERNAME TEXT NOT NULL,
	COMMENT TEXT NOT NULL,
	DATE DATE NOT NULL,
	FOREIGN KEY(USERNAME) REFERENCES user(USERNAME)
);

drop table if exists file;
create table file (
  COMMENTID INTEGER,
  IMAGE TEXT NOT NULL,
  PRIMARY KEY(COMMENTID),
  FOREIGN KEY(COMMENTID) REFERENCES comment(COMMENTID)
);

