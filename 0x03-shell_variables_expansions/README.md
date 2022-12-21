# 0x03. Shell, init files, variables and expansions

## Resources
- [Expansion](http://linuxcommand.org/lc3_lts0080.php)
- [Shell Arithmetic](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html)
- [Variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html)
- [Shell initialization files](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html)
- [The alias Command](http://www.linfo.org/alias.html)
- [Technical Writing](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2021/6/9112669886fd446a2aa3113c31319d1f468dc160.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221221%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221221T103118Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e6d79b6990afb710d86d55f0ec7e9bb27e45ffb367129369987b3b84297056c1)

## Tasks 

0. [\<o>](./0-alias) : A script that creates an alias.
   - Name of alias: `ls`
   - Value: `rm *` 
1. [Hello you](./1-hello_you) : A script that prints `hello user`, where user is the current Linux user.
2. [The path to success is to take massive, determined action](./2-path) : A script that adds `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.
3. [If the path be beautiful, let us not ask where it leads](./3-paths) : A script that counts the number of directories in the `PATH`.
4. [Global variables](./4-global_variables) : A script that prints all the enviroment variables.
5. [Local variables ](./5-local_variables) : A script that lists all local variables and enviroment variables, and functions.
6. [Local variable](./6-create_local_variable) : A script that creates a new local variable.
7. [Global variable](./7-create_global_variable) : A script that creates a new global variable.
8. [Every addition to true knowledge is an addition to human power](./8-true_knowledge) : A script that prints the results of the addition of 128 with the value stored in the enviroment variable `TRUEKNOWLEDGE`, followed by a new line.
9. [Divide and rule](./9-divide_and_rule) : A script that prints the result of `POWER` divide by `DIVIDE`, followed by a new line.
   - `POWER` and `DIVIDE` are environment variables.
10. [Love is anterior to life, posterior to death, initial of creation, and the exponent of breath](./10-love_exponent_breath) : A script that displays the result of `BREATH` to the power of `LOVE`.
    - `BREATH` and `LOVE` are enviroment variables.
    - The script should display the result, followed by a new line.
11. [There are 10 types of people in the world -- Those who understand binary, and those who don't](./11-binary_to_decimal) : A script that converts a number from base 2 to base 10.
    - The number in base 2 is stored in the enviroment variable `BINARY`.
    - The script should display the number in base 10, followed by a new line.
12. [Combination](./12-combinations) : A script that prints all possible combinations of two letters, except `oo`.
    - Letters are lower cases, from `a` to `z`.
    - One combination per line.
    - The output should be alpha ordered, starting with `aa`.
    - Do not print `oo`.
    - Your script file should contain maximum 64 characters.
13. [Floats](./13-print_float) : A script that prints a number with two decimal places, followed by a new line.
    - The number will be stored in the enviroment variable `NUM`.
14. [Decimal to Hexadecimal](./100-decimal_to_hexadecimal) : A script that converts a number from base 10 to base 16.
    - The number is base 10 is stored in the enviroment variable `DECIMAL`.
    - The script should display the number in base 16, followed by a new line.
15. [Everyone is a proponent of strong encryption](./101-rot13) : A script that encodes and decodes text using the rot13 encryption. Assume ASCII.
16. [The eggs of the brood need to be an odd number](./102-odd) : A script that prints every other line from the input, starting with the first line.
17. [I'm an instant star. Just add water and stir.](./103-water_and_stir) : A script that adds the two numbers stored in the enviroment variables `WATER` and `STIR` and prints the results.
    - `WATER` is in base `water`.
    - `STIR` is in base `stir`.
    - The result should be in base `bestchol`
