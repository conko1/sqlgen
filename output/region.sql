BEGIN
EXECUTE IMMEDIATE 'CREATE TABLE region (
    id INTEGER PRIMARY KEY,
    name VARCHAR2(21),
    abbr VARCHAR2(20)
)';

EXECUTE IMMEDIATE 'insert into region values(1, ''Banskobystrický kraj'', ''BC'')';
EXECUTE IMMEDIATE 'insert into region values(2, ''Bratislavský kraj'', ''BL'')';
EXECUTE IMMEDIATE 'insert into region values(3, ''Košický kraj'', ''KI'')';
EXECUTE IMMEDIATE 'insert into region values(4, ''Nitriansky kraj'', ''NI'')';
EXECUTE IMMEDIATE 'insert into region values(5, ''Prešovský kraj'', ''PV'')';
EXECUTE IMMEDIATE 'insert into region values(6, ''Trenčiansky kraj'', ''TC'')';
EXECUTE IMMEDIATE 'insert into region values(7, ''Trnavský kraj'', ''TA'')';
EXECUTE IMMEDIATE 'insert into region values(8, ''Žilinský kraj'', ''ZI'')';
END
/