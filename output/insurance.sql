BEGIN
EXECUTE IMMEDIATE 'CREATE TABLE insurance (
    code INTEGER PRIMARY KEY,
    name VARCHAR2(50)
)';

EXECUTE IMMEDIATE 'insert into insurance values(27, ''Union zdravotná poisťovňa'')';
EXECUTE IMMEDIATE 'insert into insurance values(25, ''Všeobecná zdravotná poisťovňa'')';
EXECUTE IMMEDIATE 'insert into insurance values(24, ''Dôvera zdravotná poisťovňa'')';
END
/