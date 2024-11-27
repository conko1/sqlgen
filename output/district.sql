BEGIN
EXECUTE IMMEDIATE 'CREATE TABLE district (
    id INTEGER PRIMARY KEY,
    code INTEGER,
    name VARCHAR2(22),
    region INTEGER,
    CONSTRAINT fk_reg_dist FOREIGN KEY (region) REFERENCES region(id)
)';

EXECUTE IMMEDIATE 'insert into district values(1, ''301'', ''Bánovce nad Bebravou'', 6)';
EXECUTE IMMEDIATE 'insert into district values(2, ''601'', ''Banská Bystrica'', 1)';
EXECUTE IMMEDIATE 'insert into district values(3, ''602'', ''Banská Štiavnica'', 1)';
EXECUTE IMMEDIATE 'insert into district values(4, ''701'', ''Bardejov'', 5)';
EXECUTE IMMEDIATE 'insert into district values(5, ''101'', ''Bratislava I'', 2)';
EXECUTE IMMEDIATE 'insert into district values(6, ''102'', ''Bratislava II'', 2)';
EXECUTE IMMEDIATE 'insert into district values(7, ''103'', ''Bratislava III'', 2)';
EXECUTE IMMEDIATE 'insert into district values(8, ''104'', ''Bratislava IV'', 2)';
EXECUTE IMMEDIATE 'insert into district values(9, ''105'', ''Bratislava V'', 2)';
EXECUTE IMMEDIATE 'insert into district values(10, ''603'', ''Brezno'', 1)';
EXECUTE IMMEDIATE 'insert into district values(11, ''501'', ''Bytča'', 8)';
EXECUTE IMMEDIATE 'insert into district values(12, ''502'', ''Čadca'', 8)';
EXECUTE IMMEDIATE 'insert into district values(13, ''604'', ''Detva'', 1)';
EXECUTE IMMEDIATE 'insert into district values(14, ''503'', ''Dolný Kubín'', 8)';
EXECUTE IMMEDIATE 'insert into district values(15, ''201'', ''Dunajská Streda'', 7)';
EXECUTE IMMEDIATE 'insert into district values(16, ''202'', ''Galanta'', 7)';
EXECUTE IMMEDIATE 'insert into district values(17, ''801'', ''Gelnica'', 3)';
EXECUTE IMMEDIATE 'insert into district values(18, ''203'', ''Hlohovec'', 7)';
EXECUTE IMMEDIATE 'insert into district values(19, ''702'', ''Humenné'', 5)';
EXECUTE IMMEDIATE 'insert into district values(20, ''302'', ''Ilava'', 6)';
EXECUTE IMMEDIATE 'insert into district values(21, ''703'', ''Kežmarok'', 5)';
EXECUTE IMMEDIATE 'insert into district values(22, ''401'', ''Komárno'', 4)';
EXECUTE IMMEDIATE 'insert into district values(23, ''802'', ''Košice I'', 3)';
EXECUTE IMMEDIATE 'insert into district values(24, ''803'', ''Košice II'', 3)';
EXECUTE IMMEDIATE 'insert into district values(25, ''804'', ''Košice III'', 3)';
EXECUTE IMMEDIATE 'insert into district values(26, ''805'', ''Košice IV'', 3)';
EXECUTE IMMEDIATE 'insert into district values(27, ''806'', ''Košice-okolie'', 3)';
EXECUTE IMMEDIATE 'insert into district values(28, ''605'', ''Krupina'', 1)';
EXECUTE IMMEDIATE 'insert into district values(29, ''504'', ''Kysucké Nové Mesto'', 8)';
EXECUTE IMMEDIATE 'insert into district values(30, ''402'', ''Levice'', 4)';
EXECUTE IMMEDIATE 'insert into district values(31, ''704'', ''Levoča'', 5)';
EXECUTE IMMEDIATE 'insert into district values(32, ''505'', ''Liptovský Mikuláš'', 8)';
EXECUTE IMMEDIATE 'insert into district values(33, ''606'', ''Lučenec'', 1)';
EXECUTE IMMEDIATE 'insert into district values(34, ''106'', ''Malacky'', 2)';
EXECUTE IMMEDIATE 'insert into district values(35, ''506'', ''Martin'', 8)';
EXECUTE IMMEDIATE 'insert into district values(36, ''705'', ''Medzilaborce'', 5)';
EXECUTE IMMEDIATE 'insert into district values(37, ''807'', ''Michalovce'', 3)';
EXECUTE IMMEDIATE 'insert into district values(38, ''303'', ''Myjava'', 6)';
EXECUTE IMMEDIATE 'insert into district values(39, ''507'', ''Námestovo'', 8)';
EXECUTE IMMEDIATE 'insert into district values(40, ''403'', ''Nitra'', 4)';
EXECUTE IMMEDIATE 'insert into district values(41, ''304'', ''Nové Mesto nad Váhom'', 6)';
EXECUTE IMMEDIATE 'insert into district values(42, ''404'', ''Nové Zámky'', 4)';
EXECUTE IMMEDIATE 'insert into district values(43, ''305'', ''Partizánske'', 6)';
EXECUTE IMMEDIATE 'insert into district values(44, ''107'', ''Pezinok'', 2)';
EXECUTE IMMEDIATE 'insert into district values(45, ''204'', ''Piešťany'', 7)';
EXECUTE IMMEDIATE 'insert into district values(46, ''607'', ''Poltár'', 1)';
EXECUTE IMMEDIATE 'insert into district values(47, ''706'', ''Poprad'', 5)';
EXECUTE IMMEDIATE 'insert into district values(48, ''306'', ''Považská Bystrica'', 6)';
EXECUTE IMMEDIATE 'insert into district values(49, ''707'', ''Prešov'', 5)';
EXECUTE IMMEDIATE 'insert into district values(50, ''307'', ''Prievidza'', 6)';
EXECUTE IMMEDIATE 'insert into district values(51, ''308'', ''Púchov'', 6)';
EXECUTE IMMEDIATE 'insert into district values(52, ''608'', ''Revúca'', 1)';
EXECUTE IMMEDIATE 'insert into district values(53, ''609'', ''Rimavská Sobota'', 1)';
EXECUTE IMMEDIATE 'insert into district values(54, ''808'', ''Rožňava'', 3)';
EXECUTE IMMEDIATE 'insert into district values(55, ''508'', ''Ružomberok'', 8)';
EXECUTE IMMEDIATE 'insert into district values(56, ''708'', ''Sabinov'', 5)';
EXECUTE IMMEDIATE 'insert into district values(57, ''108'', ''Senec'', 2)';
EXECUTE IMMEDIATE 'insert into district values(58, ''205'', ''Senica'', 7)';
EXECUTE IMMEDIATE 'insert into district values(59, ''206'', ''Skalica'', 7)';
EXECUTE IMMEDIATE 'insert into district values(60, ''709'', ''Snina'', 5)';
EXECUTE IMMEDIATE 'insert into district values(61, ''809'', ''Sobrance'', 3)';
EXECUTE IMMEDIATE 'insert into district values(62, ''810'', ''Spišská Nová Ves'', 3)';
EXECUTE IMMEDIATE 'insert into district values(63, ''710'', ''Stará Ľubovňa'', 5)';
EXECUTE IMMEDIATE 'insert into district values(64, ''711'', ''Stropkov'', 5)';
EXECUTE IMMEDIATE 'insert into district values(65, ''712'', ''Svidník'', 5)';
EXECUTE IMMEDIATE 'insert into district values(66, ''405'', ''Šaľa'', 4)';
EXECUTE IMMEDIATE 'insert into district values(67, ''406'', ''Topoľčany'', 4)';
EXECUTE IMMEDIATE 'insert into district values(68, ''811'', ''Trebišov'', 3)';
EXECUTE IMMEDIATE 'insert into district values(69, ''309'', ''Trenčín'', 6)';
EXECUTE IMMEDIATE 'insert into district values(70, ''207'', ''Trnava'', 7)';
EXECUTE IMMEDIATE 'insert into district values(71, ''509'', ''Turčianske Teplice'', 8)';
EXECUTE IMMEDIATE 'insert into district values(72, ''510'', ''Tvrdošín'', 8)';
EXECUTE IMMEDIATE 'insert into district values(73, ''610'', ''Veľký Krtíš'', 1)';
EXECUTE IMMEDIATE 'insert into district values(74, ''713'', ''Vranov nad Topľou'', 5)';
EXECUTE IMMEDIATE 'insert into district values(75, ''407'', ''Zlaté Moravce'', 4)';
EXECUTE IMMEDIATE 'insert into district values(76, ''611'', ''Zvolen'', 1)';
EXECUTE IMMEDIATE 'insert into district values(77, ''612'', ''Žarnovica'', 1)';
EXECUTE IMMEDIATE 'insert into district values(78, ''613'', ''Žiar nad Hronom'', 1)';
EXECUTE IMMEDIATE 'insert into district values(79, ''511'', ''Žilina'', 8)';
END
/