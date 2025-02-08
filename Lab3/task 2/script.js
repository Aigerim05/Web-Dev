document.querySelector('#push').onclick = function()
{
    if(document.querySelector('#newtask input').value.length == 0){
        alert("Please enter a task")
    }
    else{
        document.querySelector('#tasks').innerHTML
        += `
            <div class="task">
                <span id="taskname"><input type="checkbox">
                    ${document.querySelector
                    ('#newtask input').value}
                </span>
                <button class="delete">
                    <img src="./assets/bin.png" height=15px>
                </button>
            </div> 
        `;
        
        let current_tasks = document.querySelectorAll(".delete");
        for(let i = 0; i < current_tasks.length; i++){
            current_tasks[i].onclick = function(){
                this.parentNode.remove();
            }
        }

        let tasks = document.querySelectorAll(".task");
        for(let i = 0; i < tasks.length; i++){
            let checkbox = tasks[i].querySelector('input[type="checkbox"]');
            checkbox.onchange = function() {
                let taskText = tasks[i].querySelector('#taskname');
                if (checkbox.checked) {
                    taskText.style.textDecoration = 'line-through';
                } else {
                    taskText.style.textDecoration = 'none';
                }
            };
        }

        document.querySelector("#newtask input").value="";
        
    }
}

