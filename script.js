const taskInput=document.getElementById('task-input')
const addTaskButton=document.getElementById('add-task')
const taskList=document.getElementById('task-list')

addTaskButton.addEventListener("click", function () {
    const taskText = taskInput.value;
    if (taskText === "") {
        alert("Please enter a task!");
        return;
    }
    const taskItem = document.createElement("li");
    taskItem.textContent = taskText;

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.style.backgroundColor = "#FFD9D8";
    deleteButton.style.color = "#324e48";
    deleteButton.style.border = "none";
    deleteButton.style.cursor = "pointer";
 
    deleteButton.addEventListener("click", function () {
        taskList.removeChild(taskItem);
    });

    taskItem.appendChild(deleteButton);
    taskList.appendChild(taskItem);
    taskInput.value = "";
});
    
taskList.addEventListener("click", function (event) {
    if (event.target.tagName === 'LI') {
        event.target.style.textDecoration = event.target.style.textDecoration === "line-through" ? "none" : "line-through";
    }
});
