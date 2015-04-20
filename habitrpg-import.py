#!/usr/local/bin/python
import sys
from pyhabit import HabitAPI
from tasklib.task import TaskWarrior



def main():
    habitapi = HabitAPI("<foo>",
                        "<bar>")
    task_warrior = TaskWarrior(data_location='~/.task', create=False)
    task_warrior.config.update(
        {"uda.habitrpg-id.type":"string",
         "uda.habitrpg-id.label":"HabitRPG ID"}
        )

    #get data from habitrpg
    todos = habitapi.todos()
    #dailies = habitapi.dailies()
    #get local data from taskwarrior
    tw_todos = task_warrior.tasks.filter(tags__contains=["habitrpg"])
    print "== Taskwarriror Todos ===\n"
    for tw_todo in tw_todos:
        print tw_todo
    print "=========================\n"

    print "=== HabitRPG Todos ===\n"
    for habit_todo in todos:
        remote_name = habit_todo[u'text']
        #print "%s (%s)" % (remote_name,type(remote_name))
        local = tw_todos.filter(description__contains=remote_name)
        if local:
            print local
        # if local:
        #   print "Task %s already exists locally, checking for a habitrpg ID ..."
        #   print type(local)
        # else:
        #   print "Task %s does not exist locally creating it ..." % remote_name
    print "=======================\n"

if __name__ == "__main__":
    sys.exit(main())
