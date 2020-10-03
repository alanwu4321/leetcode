"""LOG PROCESSOR V4.6

Instructions:

Your time starts as soon as the you (the candidate) joins the pad.
You will be marked at the 90 minute mark, but you can continue developing afterwards if you desire.
The pad will not exit itself, you should exit the pad when you are done,
 by clicking the button on the bottom right.

You may solve in any language unless instructed otherwise, the examples are given in python3.6.
If you use another language, you don't have to re-implement all the examples, classes, tests, etc.
Marking focuses on the implementation of the functions, not the boilerplate.
You can also change the function signatures to whatever is more appropriate for your language.
Hints are available for some other languages at the very bottom of this page.

You can use books, google, stack overflow, etc, but don't ask for help from other people.
You may add helper functions, global variables to assist you, but avoid changing the given
function signatures.

Outline:

You are developing a log processing system, which is made up of many different "steps" that process the logs in different ways.
Each step is declared in advance, and the system is built up by feeding the output of one step into the inputs of other steps.
Each step has a python function (stored in the "action" attribute) that gets evaluated to produce the output for that step.
The user interacts with the system by telling the system they want the output of a particular step,
    and the system will call the action for that step (and any other actions that the desired step depends on) to return the processed log.

Each step is given an "output_name" attribute, which the user can use to get the output of that step. The "input_names" attribute
stores a list of strings that match the output_name from other steps, so that the output value from one step can be used as an input parameter to other steps.

Read further to see examples of the system in action, and begin with Questions 1-4.

"""
from multiprocessing.pool import ThreadPool as Pool
import multiprocessing
from datetime import datetime
from typing import List, Callable, Any

# typedef for logdata, just for clarity, since we use strings elsewhere
logdata = str

# action functions


def action_get_logs1(inputs: List[logdata]) -> logdata:
    return "this_is_a_log"


def action_get_logs2(inputs: List[logdata]) -> logdata:
    return "yet_another_log"


def action_combine_logs(inputs: List[logdata]) -> logdata:
    return " ".join(inputs)


def action_combine_logs_flipped(inputs: List[logdata]) -> logdata:
    return " ".join(reversed(inputs))


class StepDeclaration:
    def __init__(self, output_name: str, input_names: List[str], action: Callable):
        self.output_name = output_name
        self.input_names = input_names
        self.action = action


# an example of a system of step declarations for processing logs
example_system_1 = [
    StepDeclaration(
        output_name="output1",   # output_name could be any string
        input_names=[],
        action=action_get_logs1,  # action can be any python callable
    ),
    StepDeclaration(
        output_name="output2",
        input_names=[],
        action=action_get_logs2,
    ),
    StepDeclaration(
        output_name="output3",
        # each "input_names" item corresponds to an "output_name" from another StepDeclaration.
        input_names=["output1", "output2"],
        action=action_combine_logs,  # when this action function is called, the parameters to "action_combine_logs()" will be the return values from the action functions "action_get_logs1()" and "action_get_logs1()"
    ),
    StepDeclaration(
        output_name="output4",
        input_names=["output3", "output2"],
        action=action_combine_logs_flipped,
    ),
]

"""
QUESTION 1:
In example_system_1, the step for "output3" takes inputs from the steps for "output1" and "output2".
Thus, if the user requests "output3", we must first evaluate the actions for "output2" and "output1"
    to get the values of these outputs, so the values can be used as inputs to the action of "output3".

To determine the correct ordering of step dependencies, complete the action_evaluation_order()
    function below, so that it will return a list of "output_name"s needed for the "order_for_output_name" parameter.
    Each "output_name" item in the list should appear *after* any of its dependencies.
    The ordering should not contain any duplicates.

You may assume every list of "StepDeclarations" is valid and solvable, eg:
 - each "StepDeclaration" will only have one output
 - each "StepDeclaration" can have any number of dependencies (including 0)
 - a list of StepDeclarations will not contain duplicate "output_name"s
 - a "StepDeclaration" cannot depend on its own output (directly or indirectly)

For this and the following questions, assume in real life the system is running at a large scale, so efficiency is important.
That said, correct slow solutions will get more marks than incorrect fast ones.
You may also leave notes explaining where you further optimize if you had the time.
"""


def getStepsDict(step_declarations: List[StepDeclaration]):
    step_dict = dict()
    for step in step_declarations:
        step_dict[step.output_name] = step
    return step_dict


def action_evaluation_order(step_declarations: List[StepDeclaration], order_for_output_name: str) -> List[str]:
    # find the step_declaration for output name
    steps_dict = getStepsDict(step_declarations)

    visited = set()
    dependencies = list()

    def dfs(output: str):
        visited.add(output)
        for input_name in steps_dict[output].input_names:
            if not input_name in visited:
                dfs(input_name)
        dependencies.append(output)

    dfs(order_for_output_name)

    return dependencies

    """Candidate to implement."""


print("Running Q1...")
order = action_evaluation_order(
    step_declarations=example_system_1, order_for_output_name="output1")
assert order == ["output1"], "Question 1a Error"

order = action_evaluation_order(
    step_declarations=example_system_1, order_for_output_name="output2")
assert order == ["output2"], "Question 1b Error"

order = action_evaluation_order(
    step_declarations=example_system_1, order_for_output_name="output3")
# order should be a list of strings which are in the following order
assert order in (
    ["output1", "output2", "output3"],
    ["output2", "output1", "output3"],
), "Question 1c Error"  # there are multiple valid orders for "output3"


order = action_evaluation_order(
    step_declarations=example_system_1, order_for_output_name="output4")
assert order in (
    ["output1", "output2", "output3", "output4"],
    ["output2", "output1", "output3", "output4"],
), "Question 1d Error"  # there are multiple valid orders for "output4"
print("Q1 OK")

"""
QUESTION 2:
Now that we know the order in which the actions have to be evaluated, complete the
  get_output_value() function below so that it calls each "action" in
  the correct order with the right input(s), and returns the output value of
  the "action" function for the StepDeclaration where the output_name attribute
  matches the "output_name" parameter.

You can use your previous working if desired.

for example_system_1, the get_output_value(example_system_1, "output3") function will do the following
1) call action_get_logs1(), and store the output
2) call action_get_logs2(), and store the output
3) call action_combine_logs(), with the output from 1) and 2) as the input
4) return the result of 3), as the "value_for_output_name" parameter matches the StepDeclaration.output_name for that step.
# note that as in Q1, step 1) and 2) could happen in the reverser order.
"""


def get_output_value(step_declarations: List[StepDeclaration], value_for_output_name: str) -> logdata:
    steps_dict = getStepsDict(step_declarations)
    steps_dependencies = action_evaluation_order(
        step_declarations, value_for_output_name)

    action_outputs = dict()

    for dep in steps_dependencies:
        # temp = map(lambda x: action_outputs[x], steps_dict[dep].input_names)
        outputs = list()
        # single step doesn't have any input dependency
        for inp in steps_dict[dep].input_names:
            outputs.append(action_outputs[inp])
        # store results in the map so we can later retrieve 
        action_outputs[dep] = steps_dict[dep].action(outputs)
        print(action_outputs)
        print(outputs)
    return action_outputs[value_for_output_name]

    """Candidate to implement.

    Parses the "step_declarations" parameter to call the appropriate "actions" in the correct order.
    The input(s) to each "action" are outputs of previous "actions".
    Return the output value of the action corresponding to the "output_name".
    """


print("Running Q2...")
out1 = get_output_value(step_declarations=example_system_1,
                        value_for_output_name="output1")
assert out1 == "this_is_a_log", "Question 2a Error"

out3 = get_output_value(step_declarations=example_system_1,
                        value_for_output_name="output3")
assert out3 == "this_is_a_log yet_another_log", "Question 2b Error"

out4 = get_output_value(step_declarations=example_system_1,
                        value_for_output_name="output4")
assert out4 == "yet_another_log this_is_a_log yet_another_log", "Question 2c Error"
print("Q2 OK")


"""
QUESTION 3:
We expect the "get_output_value()" function to be called multiple times with varying "step_declarations" and "value_for_output_name"s.
As some of the "actions" might be expensive to call, we should cache the output of "action" calls.
That way, if an "action" is called multiple times with the same input values, the output value can be reused without recomputing.
An "action" function may be re-used multiple in many "StepDeclarations" within one system, or within different systems sharing a cache.

Implement get_output_value_with_caching() below to use the global "cache" variable.

"actions" are pure functions, where the output value of each function only depends on the values of the inputs. In
a real system, some inputs are accessing external data (eg, reading logs off a filesystem) rather than just fixed strings like the examples given. We can simulate this by having one of the steps that takes no inputs return a variable result.
"""

# new actions and system for Q3


def action_read_logs(inputs: List[logdata]) -> logdata:
    return f"log from a file system at {datetime.now().minute}"


def action_combine_logs(inputs: List[logdata]) -> logdata:
    return " ".join(inputs)


example_system_2 = [
    StepDeclaration(
        output_name="read_output",
        input_names=[],
        action=action_read_logs,
    ),
    StepDeclaration(
        output_name="fixed_output",
        input_names=[],
        action=action_get_logs1,
    ),
    StepDeclaration(
        output_name="system_2_output",
        input_names=["read_output", "fixed_output"],
        action=action_combine_logs,
    ),
]

cache = {}  # use this variable as your cache


def get_output_value_with_caching(step_declarations: List[StepDeclaration], value_for_output_name: str) -> logdata:
    steps_dict = getStepsDict(step_declarations)
    steps_dependencies = action_evaluation_order(
        step_declarations, value_for_output_name)

    action_outputs = dict()

    for dep in steps_dependencies:
        # temp = map(lambda x: action_outputs[x], steps_dict[dep].input_names)
        outputs = list()
        for inp in steps_dict[dep].input_names:
            outputs.append(action_outputs[inp])
        action = steps_dict[dep].action

        pair = cache[action] if action in cache else None

        # pair = duple(output, input)
        if not pair or not pair[0] == outputs:
            cache[action] = (outputs, action(outputs))

        # store input
        action_outputs[dep] = cache[action][1]

    return action_outputs[value_for_output_name]

    """Candidate to implement."""


print("Running Q3...")
get_output_value_with_caching(
    step_declarations=example_system_2, value_for_output_name="system_2_output")
# values added to the cache during this call
get_output_value_with_caching(
    step_declarations=example_system_2, value_for_output_name="system_2_output")
# In the second call, if the output for "read_output" is the same as the first call, then
# that means that the inputs for "system_2_output" haven't changed, which means we don't
# need to recalculate the output value for "system_2_output".
# If the output for action_read_logs changes, then we should recalculate "system_2_output"

"""
QUESTION 4:
Another performance upgrade would be to add concurrency/parallelism where possible to increase the performance of the system.
One example of this, in example_system_1, is that a single-threaded system will wait for the result of action_get_logs1() before calling action_get_logs2() (or vice versa).
However these functions are independent of eachother and could be executed in parallel, speeding up the system.

Complete the "get_output_value_with_caching_and_parallelism" below, using concurrency/parallelism anywhere possible to
 increase the performance of the system.

Your selection of parallelization primitive or library does not affect your score
 (eg, you may use multithreading, multiprocessing, asyncio, etc)

You can assume that there is no performance overhead for additional workers
(eg, you have unlimited CPUs), and that all action functions are IO-bound.

Extra for experts: limit the number of CPU cores you have to N, and assume each action can utilize
 a fixed number of CPUs from 1 to N. Then schedule parallel actions such that CPU cores
 are optimally utilized (but not oversaturated).
"""

# an example of a system of step declarations for processing logs
example_system_1 = [
    StepDeclaration(
        output_name="output1",   # output_name could be any string
        input_names=[],
        action=action_get_logs1,  # action can be any python callable
    ),
    StepDeclaration(
        output_name="output2",
        input_names=[],
        action=action_get_logs2,
    ),
    StepDeclaration(
        output_name="output3",
        # each "input_names" item corresponds to an "output_name" from another StepDeclaration.
        input_names=["output1", "output2"],
        action=action_combine_logs,  # when this action function is called, the parameters to "action_combine_logs()" will be the return values from the action functions "action_get_logs1()" and "action_get_logs1()"
    ),
    StepDeclaration(
        output_name="output4",
        input_names=["output3", "output2"],
        action=action_combine_logs_flipped,
    ),
]


def get_output_value_with_parallelism(step_declarations: List[StepDeclaration], value_for_output_name: str) -> logdata:
    steps_dict = getStepsDict(step_declarations)
    steps_dependencies = action_evaluation_order(
        step_declarations, value_for_output_name)

    action_outputs = dict()

    pool = Pool(multiprocessing.cpu_count() - 1)

    def func(dep):
        for inp in steps_dict[dep].input_names:
            while (inp not in action_outputs):
                pass
        outputs = list()
        for inp in steps_dict[dep].input_names:
            outputs.append(action_outputs[inp])
        action = steps_dict[dep].action
        pair = cache[action] if action in cache else None

        # pair = [output, input]
        if not pair or not pair[0] == outputs:
            cache[action] = [outputs, action(outputs)]

        action_outputs[dep] = cache[action][1]

    pool.map(func, steps_dependencies)

    return action_outputs[value_for_output_name]


print("Running Q4...")
print(get_output_value_with_parallelism(
    step_declarations=example_system_2, value_for_output_name="system_2_output"))

"""
*** OTHER LANGAUGE EXAMPLES ***

*** Java (11) ***
// functions are not first-class objects in java
// but we can use lambdas and interfaces instead.
import java.io.*;
import java.util.*;

interface ActionFunction {
    public String run(List<String> inputs);
}

class Step {
    public String output;
    public List<String> inputs;
    public ActionFunction action;
    public Step(String out, List<String> in, ActionFunction a) {
        inputs = in;
        output = out;
        action = a;
    }
}

class Solution {
  public static void main(String[] args) {

    ActionFunction joiner = (inputs) -> {
      return String.join(" ", inputs);
    };

    Step a_step = new Step(
      "output",
      List.of("input1", "input2"),
      joiner
    );

    var out = a_step.action.run(List.of("this_is_a_log", "another_log"));
    System.out.println(out);
  }
}

*** Rust ***
// fairly straight forward.
// however note the extra parentheses here around the
// "action" member of the step struct to call the
// function properly.
fn action_join(inputs: Vec<String>) -> String {
    inputs.join(" ")
}

type Action = fn(Vec<String>) -> String;

pub struct Step {
    output_name: String,
    input_names: Vec<String>,
    action: Action,
}

fn main() {
    let a_step = Step {
        input_names: vec![
            "in1".to_string(),
            "in2".to_string(),
        ],
        output_name: "out1".to_string(),
        action: action_join,
    };

    // note the extra parentheses here around the struct member.
    let result = (a_step.action)(vec![
        "lifetimes".to_string(),
        "are".to_string(),
        "fun".to_string(),
    ]);

    println!("{}", result);
}

"""
