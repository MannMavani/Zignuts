class University {
    constructor(name) {
        this.name = name;
        this.departments = [];
    }

    addDepartment(dept) {
        this.departments.push(dept);
    }

    removeDepartment(dept) {
        this.departments = this.departments.filter(d => d !== dept);
    }

    displayDepartments() {
        console.log(`Departments in ${this.name}:`, this.departments.join(", "));
    }
}


const uni = new University("ABC University");
uni.addDepartment("Computer Science");
uni.addDepartment("Mechanical");
uni.addDepartment("Civil");
uni.displayDepartments();

uni.removeDepartment("Civil");
uni.displayDepartments();
