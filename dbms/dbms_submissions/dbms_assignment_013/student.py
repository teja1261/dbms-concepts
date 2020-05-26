class InvalidField(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class DoesNotExist(Exception):
    pass

class Student:
    def __init__(self, name, age, score, student_id = None):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.score = score
        
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(self.student_id,self.name,self.age,self.score)
        
    @classmethod
    def get(cls,**kargs):
        list = ['student_id','name','age','score']
        
        for i in kargs:
            if i not in list:
                raise InvalidField
            
        import sqlite3
        connection = sqlite3.connect("selected_students.sqlite3")
        crsr = connection.cursor()
        
        for i,j in kargs.items():
            if kargs[i] != None:
                if i != 'name':
                    query = "SELECT * FROM Student WHERE {} = {}".format(i,j)
                else:
                    query = "SELECT * FROM Student WHERE {} = '{}'".format(i,j)
                    
        crsr.execute(query)
        ans= crsr.fetchall()
        
        if len(ans) > 1:
            raise MultipleObjectsReturned
            
        if ans == []:
            raise DoesNotExist
        
        connection.close()
        
        student_obj = Student(student_id = ans[0][0],name = ans[0][1],age = ans[0][2],score = ans[0][3])
        
        return student_obj
    
    def delete(self):
        import sqlite3
        connection = sqlite3.connect("selected_students.sqlite3")
        crsr = connection.cursor()
        crsr.execute("DELETE FROM Student WHERE student_id = {}".format(self.student_id))
        connection.commit()
        connection.close()
        
    def save(self):
        import sqlite3
        connection = sqlite3.connect("selected_students.sqlite3")
        crsr = connection.cursor()
        crsr.execute("SELECT student_id FROM Student WHERE student_id = ?",(self.student_id,))
        a = crsr.fetchall()
        if self.student_id == None:
            crsr.execute("INSERT INTO Student(name,age,score)VALUES(?,?,?)",(self.name,self.age,self.score))
            self.student_id = crsr.lastrowid
        
        elif a == []:
            crsr.execute("INSERT or REPLACE INTO Student(student_id,name,age,score)VALUES(?,?,?,?)",(self.student_id,self.name,self.age,self.score))
        
        else:
            crsr.execute("UPDATE Student SET name = ?,age = ?,score = ? WHERE student_id = ?",(self.name,self.age,self.score,self.student_id))
        
        connection.commit()
        connection.close()
        
    @classmethod    
    def filter(cls, **kargs):
        
        list = ['student_id','name','age','score']
        
        filter_obj = []
        
        multiple_values = []
        
        import sqlite3
        connection = sqlite3.connect("selected_students.sqlite3")
        crsr = connection.cursor()
        
        for i,j in kargs.items():
            
            a = i.split('__')
            
            if a[0] not in list:
                raise InvalidField
                
            oper = {'gt':'>', 'lt':'<', 'lte':'<=', 'gte':'>=', 'neq':'<>', 'eq' : '='}
            
            if len(a) == 1:
                val = "{} {} '{}' ".format(a[0],oper['eq'],j)
                
            elif a[1] == 'in':
                j = tuple(j)
                val = "{} {} {}".format(a[0],'IN',j)
            
            elif a[1] == 'contains':
                val = "{} {} '%{}%' ".format(a[0],'LIKE',j)
                
            else:
                val = "{} {} '{}' ".format(a[0],oper[a[1]],j)
                
            multiple_values.append(val)
        
        
        x = ' AND '.join(multiple_values)
        
        crsr.execute("SELECT * FROM Student WHERE {}".format(x))
        ans = crsr.fetchall()
        
        for obj in ans:
            filter_obj.append(cls(student_id = obj[0],name = obj[1],age = obj[2],score = obj[3]))
                
        connection.commit()
        connection.close()
        
        return filter_obj
