CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    fname VARCHAR(20) NOT NULL, 
    lname VARCHAR(20) NOT NULL,
    salary INTEGER,
    full_time BOOLEAN DEFAULT True NOT NULL,
    start_date DATE,
    dept_code VARCHAR(5)
        REFERENCES Departments
    );


CREATE TABLE departments(
    dept_code VARCHAR(5) PRIMARY KEY,
    dept VARCHAR(20) NOT NULL,
    phone VARCHAR(20));

INSERT INTO departments VALUES ('mktg', 'Marketing', '555-1212');
INSERT INTO departments VALUES ('legal', 'Legal', '555-1000');

INSERT INTO employees (fname, lname, dept_code, salary) 
    VALUES ('Leonard', 'Lancelot', 'legal', 100000);

INSERT INTO employees (fname, lname, dept_code, salary)
    VALUES ('Maggie', 'McEnroe', 'mktg', 70000);

INSERT INTO employees (fname, lname, dept_code, salary)
    VALUes ('Liz', 'Lemon', 'legal', 9000);


INSERT INTO employees (fname, lname, salary, full_time, dept_code)
    SELECT 'Leon', 'Lansing', salary, full_time, dept_code
    FROM Employees
    WHERE id=1;


BEGIN;

INSERT INTO checking (acct, amt) VALUES ('ABC123', -100);
INSERT INTO savings (acct, amt) VALUES ('ABC123', 100);

COMMIT;
