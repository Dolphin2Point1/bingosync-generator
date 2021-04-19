# Bingosync-Generator

Generates [bingosync](https://bingosync.com/) json!

## Creating a choice pool

Before you can use this program, you need to create a choice pool. What is a choice pool? It pools all the possible 
choices. These choices are picked from randomly, and put onto a bingo entry.

You have two options for making a bingo board. YAML, or spreadsheet. I recommend you use yaml.

### Yaml (Recommended)

Yaml is a data storage format that is designed to be easy to read, and use. To use yaml to create our choice pool, we 
need to create a list of possible choices (in text) in a group called 'choices'. But how do we do that?

First, create a file that ends in '.yaml'. An example could be "bingosync.yaml". In there we will put these contents
```yaml
choices:
  - this
  - is
  - where
  - you
  - put
  - your
  - possible
  - choices 
```
Woah, slow down! What is that doing! First off, yaml is just lists of keys. In this case the key is 'choices'. Then when
we hit the newline, yaml realizes "oh, this key can contain more keys, or a list". Then by putting - we tell yaml "hey 
this is a list entry!". For every list entry we put a "-", then a piece of text that we want to be a choice in a choice 
pool. Let's take for example we want one of the choices to be "Tame a wolf", another to be "Kill 2 zombies", and a final
one to be "Reach bedrock", because we are playing minecraft. We can then put: 
```yaml
choices:
  - Tame a wolf
  - Kill 2 zombies
  - Reach bedrock
```
### **However, we must have atleast 25 choices, because that's how many we have on the board. Optimally you'd have several times more than that, so random boards can be chosen each time.** 

When done, go to "Using" to continue.

### Excel

Excel is a spreadsheet format, that requires a spreadsheet editing software. If you don't have one, and you don't want 
to go to google sheets, you must use yaml. To use a spreadsheet, you need to create a column, and at the top of the 
column, you need to give it the title "Bingo Choices". Then you can put them in the first column, and export it in the 
format of your choice. When done, go to "Using" to continue.

### **However, we must have atleast 25 choices, because that's how many we have on the board. Optimally you'd have several times more than that, so random boards can be chosen each time.** 

## Using

To use the program, you'll need to run it and specify the input file, and optionally the output file.

```
-o = output file
-y = yaml file
-e = spreadsheet
```

For example, if you want to read in from a yaml file named "aaaaaa.yaml" and output it to the default output.json 
location:
```bash
python main.py -y aaaaaa.yaml
```
Another example, if you want to read in a spreadsheet named "yes.xlsx" and output it to "testing.json":
```bash
python main.py -e excel.xlsx
```
Then, go to [bingosync](https://bingosync.com/), and select "Custom (Advanced)" as the game. Put the json into the area
named "Board". Then fill out the rest as normal.
