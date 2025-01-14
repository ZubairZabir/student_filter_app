import sqlite3

# Connect to the database (it will create it if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Drop the table if it exists to avoid issues with column mismatch
cursor.execute('DROP TABLE IF EXISTS students')

# Create the table with 10 columns
cursor.execute('''
CREATE TABLE students (
    last_name TEXT,
    first_name TEXT,
    student_number TEXT,
    spring_hall TEXT,
    spring_room TEXT,
    maymester_hall TEXT,
    maymester_room TEXT,
    email TEXT,
    move_in_date TEXT,
    move_out_date TEXT
)
''')

# Insert the data extracted from the image
students = [
    ('Vlasova', 'Polina', 'R01205010', 'Lakeside Neighborhood', '1326C', 'Sutton Apartments', '208B', 'pvlasova@rollins.edu', '2024-05-17', '2024-06-02'),
    ('Nurse', 'Savannah', 'R01208416', 'Lakeside Neighborhood', '1328C', 'Sutton Apartments', '211B', 'snurse@rollins.edu', '2024-05-17', '2024-07-28'),
    ('Tiangbe', 'Yole', 'R01210254', 'Lakeside Neighborhood', '1340A', 'Sutton Apartments', '210B', 'ytiangbe@rollins.edu', '2024-05-17', '2024-07-10'),
    ('Christopher', 'Dare\'one', 'R01205475', 'Lakeside Neighborhood', '1226A', 'Sutton Apartments', '311A', 'dchristopher@rollins.edu', '2024-05-17', '2024-07-28'),
    ('Lomba', 'Sofia', 'R01209767', 'Lakeside Neighborhood', '1329A', 'Sutton Apartments', '311A', 'slomba@rollins.edu', '2024-05-17', '2024-06-02'),
    ('Kim', 'Katherine', 'R01208699', 'Lakeside Neighborhood', '2205C', 'Sutton Apartments', '210A', 'kkim@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Ligay', 'Polina', 'R01216542', 'Lakeside Neighborhood', '1326A', 'Sutton Apartments', '219A', 'pligay@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Boland', 'Danielle', 'R01216863', 'Lakeside Neighborhood', '1416B', 'Sutton Apartments', '219A', 'dboland@rollins.edu', '2024-05-17', '2024-06-23'),
    ('Kramer', 'Olivia', 'R01217384', 'Lakeside Neighborhood', '1407A2', 'Sutton Apartments', '209B', 'okramer@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Inscore', 'Janie', 'R01219347', 'Lakeside Neighborhood', '1324C', 'Sutton Apartments', '219B', 'jinscore@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Amon', 'Victoria', 'R01219423', 'Sutton Apartments', '312A', 'Sutton Apartments', '312A', 'vamon@rollins.edu', '2024-05-17', '2024-07-28'),
    ('Bokash', 'Jackson', 'R01219880', 'Lakeside Neighborhood', '2204B', 'Sutton Apartments', '310B', 'jbokash@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Wade', 'Jessica', 'R01218836', 'Lakeside Neighborhood', '1513C', 'Sutton Apartments', '209B', 'jrwade@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Martinborough', 'Bree', 'R01219286', 'Lakeside Neighborhood', '1504', 'Sutton Apartments', '318', 'bmartinborough@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Grishaev', 'Sergey', 'R01223571', 'Holt Hall', '305', 'Sutton Apartments', '310A', 'sgrishaev@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Manitz', 'Hailey', 'R01221049', 'Lakeside Neighborhood', '1518D', 'Sutton Apartments', '211A', 'hmanitz@rollins.edu', '2024-05-17', '2024-07-21'),
    ('Hussey', 'Sarah', 'R01216750', 'Lakeside Neighborhood', '1313A', 'Sutton Apartments', '203B', 'shussey@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Campbell', 'Henry', 'R01219240', 'Lakeside Neighborhood', '1516B', 'Sutton Apartments', '205A', 'hcampbell@rollins.edu', '2024-05-17', '2024-06-16'),
    ('Manchanda', 'Jiya', 'R01216993', 'Lakeside Neighborhood', '1236B', 'Sutton Apartments', '218', 'jmanchanda@rollins.edu', '2024-05-17', '2024-07-14'),
    ('Tessler', 'Evan', 'R01220684', 'Lakeside Neighborhood', '2304D', 'Sutton Apartments', '320B', 'etessler@rollins.edu', '2024-05-17', '2024-06-09'),
    ('Kunda', 'Bupe', 'R01218580', 'Lakeside Neighborhood', '1420B', 'Sutton Apartments', '211B', 'bkunda@rollins.edu', '2024-05-17', '2024-07-21'),
    ('Reynolds', 'Emily', 'R01221333', 'Lakeside Neighborhood', '2410D', 'Sutton Apartments', '318', 'ereynolds@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Gara Grady', 'Aislinn', 'R01221894', '', '', 'Sutton Apartments', '211A', 'agaragrady@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Mwiinga', 'Nchimunya', 'R01218436', 'Lakeside Neighborhood', '2204D', 'Sutton Apartments', '314A', 'nmwiinga@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Goldberg', 'Michael', 'R01220445', 'Lakeside Neighborhood', '1516D', 'Sutton Apartments', '205A', 'mgoldberg@rollins.edu', '2024-05-17', '2024-07-14'),
    ('King', 'Victoria', 'R01224019', 'Lakeside Neighborhood', '1318C', 'Sutton Apartments', '208B', 'vking@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Kluger', 'Paloma', 'R01218920', 'Lakeside Neighborhood', '1330A', 'Sutton Apartments', '208A', 'pkluger@rollins.edu', '2024-05-17', '2024-07-07'),
    ('Iloghalu', 'Chukwuebuka', 'R01223175', 'Lakeside Neighborhood', '1109A1', 'Sutton Apartments', '314B', 'ciloghalu@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Klanot', 'Selby', 'R01229097', 'Lakeside Neighborhood', '1324A', 'Sutton Apartments', '219B', 'sklanot@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Prelog', 'Olivia', 'R01227169', 'Lakeside Neighborhood', '2203B', 'Sutton Apartments', '311B', 'oprelog@rollins.edu', '2024-05-17', '2024-07-07'),
    ('Hemberger', 'Kaitlyn', 'R01230709', 'Lyman Hall', '311', 'Sutton Apartments', '203A', 'khemberger@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Nguyen', 'Moc Lan', 'R01231578', 'Sutton Apartments', '209A', 'Sutton Apartments', '209A', 'mnguyen1@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Griggs', 'Kavon', 'R01194383', 'Holt Hall', '404', 'Sutton Apartments', '310B', 'kgriggs@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Tesser', 'Alice', 'R01237045', 'Sutton Apartments', '110A', 'Sutton Apartments', '209A', 'atesser@rollins.edu', '2024-05-17', '2024-07-07'),
    ('Massaro', 'Rian', 'R01230562', 'Sutton Apartments', '415B', 'Sutton Apartments', '307', 'rmassaro@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Zabir', 'Zubair', 'R01231020', 'Sutton Apartments', '308B', 'Sutton Apartments', '308B', 'zzabir@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Ryan', 'Penelope', 'R01234934', 'Mayflower Hall', '209', 'Sutton Apartments', '317', 'pryan@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Barcelo', 'Emily', 'R01230896', 'Sutton Apartments', '214A', 'Sutton Apartments', '214A', 'ebarcelo@rollins.edu', '2024-05-17', '2024-07-21'),
    ('Hall', 'James', 'R01237799', 'Lakeside Neighborhood', '1120C', 'Sutton Apartments', '205B', 'jhall@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Walker', 'Shyhiem', 'R01238128', 'Sutton Apartments', '114A', 'Sutton Apartments', '309B', 'srwalker@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Pimentel', 'Valeria', 'R01244115', 'Elizabeth Hall', '219', 'Sutton Apartments', '312A', 'vpimentel@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Pasternak', 'Kaylie', 'R01243628', 'Strong Hall 219', '153', 'Sutton Apartments', '214B', 'kpasternak@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Liriano', 'Hailey', 'R01242551', 'Elizabeth Hall', '115', 'Sutton Apartments', '210B', 'hliriano@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Santiago Sanchez', 'Karen', 'R01240429', 'Mayflower Hall', '206', 'Sutton Apartments', '204A', 'ksantiagosanchez@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Pruna-Garcia', 'Kiara', 'R01242894', 'Strong Hall 219', '251', 'Sutton Apartments', '319A', 'kprunagarcia@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Alorda', 'Diego', 'R01245868', 'Ward Hall', '357', 'Sutton Apartments', '309B', 'dalorda@rollins.edu', '2024-05-17', '2024-06-23'),
    ('Benander', 'Tuesday', 'R01246656', 'Elizabeth Hall', '206', 'Sutton Apartments', '319B', 'tbenander@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Gasparini', 'Ollie', 'R01228603', 'Holt Hall', '206', 'Sutton Apartments', '217', 'bgasparini@rollins.edu', '2024-05-17', '2024-08-04'),
    ('Nazarenko', 'Vadim', 'R01201278', 'Rex Beach Hall', '212', 'Ward Hall', '260', 'vnazarenko@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Alexander', 'August', 'R01200343', 'Lakeside Neighborhood', '1520C', 'Ward Hall', '161', 'aalexander1@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Whitney', 'Elizabeth', 'R01208713', 'Lakeside Neighborhood', '1402C', 'Ward Hall', '239', 'ewhitney@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Andrews', 'Vernon', 'R01211296', 'Lakeside Neighborhood', '1109B2', 'Ward Hall', '110', 'vlandrews@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Heliou Le Heux', 'Kalliopi', 'R01210597', 'Cross Hall', '209', 'Ward Hall', '234', 'kheliouleheux@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Delgado', 'Osman', 'R01211395', 'Lakeside Neighborhood', '1114A', 'Ward Hall', '114', 'oadelgado@rollins.edu', '2024-05-17', '2024-06-08'),
    ('McClear', 'John', 'R01215270', 'Lakeside Neighborhood', '1406D', 'Ward Hall', '257', 'jmcclear@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Meekins', 'Lilah', 'R01216007', 'Lakeside Neighborhood', '1338B', 'Ward Hall', '238', 'lmeekins@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Riera', 'Felix', 'R01220416', 'Hooker Hall', '208', 'Ward Hall', '123', 'frieria@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Moreland', 'Millicent', 'R01221007', 'Cross Hall', '105', 'Ward Hall', '231', 'mmoreland1@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Brown', 'Katelyn', 'R01222379', 'Corrin Hall', '109', 'Ward Hall', '210', 'kgbrown@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Rovira Monterrosa', 'Conrado', 'R01223442', 'Lakeside Neighborhood', '2403C', 'Ward Hall', '115', 'croviramonterrosa@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Knowles', 'Shalisa', 'R01216494', 'Lakeside Neighborhood', '1503', 'Ward Hall', '218', 'seknowles@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Giovannelli', 'Matthew', 'R01218197', 'Hooker Hall', '302', 'Ward Hall', '115', 'mgiovannelli@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Vega', 'Ana', 'R01216633', 'Lakeside Neighborhood', '1106C', 'Ward Hall', '211', 'arvega@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Pi', 'Jorge', 'R01216713', 'Lakeside Neighborhood', '1330C', 'Ward Hall', '157', 'jpi@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Foropoulos', 'Allison', 'R01219182', 'Lakeside Neighborhood', '1223B1', 'Ward Hall', '211', 'aforopoulos@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Thomson', 'Sarah', 'R01218989', 'Sutton Apartments', '207', 'Ward Hall', '214', 'sthomson@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Greco', 'Jaclyn', 'R01218442', 'Sutton Apartments', '401B', 'Ward Hall', '213', 'jtgreco@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Lockhart', 'Ava', 'R01219319', 'Pinehurst', '203', 'Ward Hall', '207', 'alockhart@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Fritsch', 'Miranda', 'R01219935', 'Sutton Apartments', '506', 'Ward Hall', '213', 'mfritsch@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Koster', 'Isabella', 'R01223489', 'Sutton Apartments', '207', 'Ward Hall', '214', 'ikoster@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Rooth', 'Jack', 'R00999172', 'Sutton Apartments', '520A', 'Ward Hall', '119', 'jrooth@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Pfaffenberger', 'Walter', 'R01227431', 'Sutton Apartments', '303B', 'Ward Hall', '121', 'wpfaffenberger@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Owen', 'Erica', 'R01227790', 'Mayflower Hall', '101', 'Ward Hall', '215', 'eowen@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Lahuti', 'Daniel', 'R01229074', 'Holt Hall', '212', 'Ward Hall', '254', 'dlahuti@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Robbins', 'Alex', 'R01229741', 'Holt Hall', '317', 'Ward Hall', '259', 'alrobbins@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Vaughn', 'Charles', 'R01229769', 'Sutton Apartments', '109A', 'Ward Hall', '121', 'cvaughn@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Doherty', 'Celia', 'R01230025', 'Sutton Apartments', '501A', 'Ward Hall', '212', 'cdoherty@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Sherrer', 'Sarah', 'R01231309', 'Lyman Hall', '100', 'Ward Hall', '218', 'ssherrer@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Larsen', 'Lilah', 'R01232266', 'Holt Hall', '413', 'Ward Hall', '210', 'lslarsen@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Duntley', 'Reese', 'R01233602', 'Cross Hall', '303', 'Ward Hall', '110', 'rduntley@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Demetriades', 'Constantine', 'R01236137', 'Sutton Apartments', '306', 'Ward Hall', '257', 'cdemetriades@rollins.edu', '2024-05-17', '2024-06-08'),
    ('De Miguel Pavon', 'Alejandro', 'R01234726', 'Hooker Hall', '215', 'Ward Hall', '123', 'ademiguelpavon@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Tucker', 'Ian', 'R01231887', 'Holt Hall', '313', 'Ward Hall', '113', 'itucker@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Mccullen', 'Samuel', 'R01234390', 'Sutton Apartments', '306', 'Ward Hall', '155', 'smccullen@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Hollmann', 'Weston', 'R01237171', 'Holt Hall', '317', 'Ward Hall', '155', 'whollmann@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Barker', 'Gavin', 'R01226759', 'Gale Hall', '221', 'Ward Hall', '119', 'gbarker@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Mathieu', 'Eli', 'R01235345', 'Lakeside Neighborhood', '1110C', 'Ward Hall', '259', 'emathieu@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Pikus', 'Benjamin', 'R01229379', 'Gale Hall', '114', 'Ward Hall', '113', 'bpikus@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Rubinsky', 'Gabriel', 'R01232779', 'Lakeside Neighborhood', '1107A', 'Ward Hall', '261', 'grubinsky@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Reid-Kirkland', 'Isaiah', 'R01236895', 'Sutton Apartments', '114B', 'Ward Hall', '156', 'ireidkirkland@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Becker', 'Jonathan', 'R01231427', 'Holt Hall', '210', 'Ward Hall', '263', 'jtbecker@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Knowles', 'Taneil', 'R01238844', 'Sutton Apartments', '114A', 'Ward Hall', '156', 'tknowles@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Whelan', 'Emily', 'R01240492', 'Elizabeth Hall', '213', 'Ward Hall', '221', 'ewhelan@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Kirkeide', 'Anders', 'R01242393', 'Ward Hall', '161', 'Ward Hall', '161', 'akirkeide@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Lin', 'Logan', 'R01242473', 'Holt Hall', '401', 'Ward Hall', '157', 'llin@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Becnel', 'Annabella', 'R01244556', 'Elizabeth Hall', '156', 'Ward Hall', '237', 'abecnel@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Bahadoorsingh', 'Catherine', 'R01244663', 'Elizabeth Hall', '222', 'Ward Hall', '223', 'cbahadoorsingh@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Baker', 'Layne', 'R01247977', 'Ward Hall', '457', 'Ward Hall', '223', 'lmbaker@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Macdonald', 'John', 'R01239795', 'Rex Beach Hall', '203', 'Ward Hall', '221', 'jmacdonald@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Ortega', 'Yenny', 'R01250274', 'Lakeside Neighborhood', '1103A2', 'Ward Hall', '236', 'yortega@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Dohr', 'Cecelia', 'R01240459', 'Elizabeth Hall', '305', 'Ward Hall', '227', 'cdohr@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Rodriguez', 'Liliana', 'R01241880', 'Ward Hall', '219', 'Ward Hall', '219', 'lmrodriguez@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Reyes', 'Mariana', 'R01247703', 'Rex Beach Hall', '303', 'Ward Hall', '229', 'mreyes@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Kubiak', 'Katie', 'R01248080', 'Ward Hall', '339', 'Ward Hall', '215', 'kkubiak@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Nelson', 'Clark', 'R01241681', 'Strong Hall 219', '243', 'Ward Hall', '255', 'cenelson@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Blick', 'Katherine', 'R01242332', 'Ward Hall', '228', 'Ward Hall', '228', 'kblick@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Pool', 'Chloe', 'R01243200', 'Ward Hall', '417', 'Ward Hall', '235', 'cpool@rollins.edu', '2024-05-17', '2024-06-08'),
    ('De Giacomo', 'Nicolas', 'R01250593', 'Elizabeth Hall', '306', 'Ward Hall', '117', 'ndegiacomo@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Davis', 'Emily', 'R01240604', 'Elizabeth Hall', '305', 'Ward Hall', '227', 'endavis@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Bolivar', 'Juan', 'R01251162', 'Lakeside Neighborhood', '1412B1', 'Ward Hall', '114', 'jbolivar@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Wiersema', 'Lilly', 'R01247525', 'Ward Hall', '413', 'Ward Hall', '235', 'lwiersema@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Pena Peguero', 'Helen', 'R01251154', 'Sutton Apartments', '502S', 'Ward Hall', '229', 'hpenapeguero@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Jorge', 'Alexandra', 'R01244992', 'Elizabeth Hall', '225', 'Ward Hall', '237', 'ajorge@rollins.edu', '2024-05-17', '2024-06-08'),
    ('Butera', 'Nash', 'R01236749', 'Sutton Apartments', '520B', 'Ward Hall', '255', 'nbutera@rollins.edu', '2024-05-17', '2024-06-08')
]


# Insert the data into the table
cursor.executemany('INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', students)
conn.commit()
conn.close()
