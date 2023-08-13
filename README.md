# SlimeFun Crafting Calculator

**A program for calculating crafting steps and raw material requirements for SlimeFun items.**

I may give this a proper GUI at some point, but right now it's just a basic console app.

## General usage
List the items you want to craft in *input.sf*, in the following syntax:
> `10*reinforced_alloy`
> 
> `1*electromagnet`

List exactly one item per line. Do not leave blank lines. Quantities must always be listed at the start and demarcated with a star, even when equal to 1.

**Conventions for item names:**
Item names use all-lowercase, and underscores instead of spaces (e.g. "zinc_ingot").
Item names are spelled and worded exactly as written in game (e.g. "reinforced_alloy" instead of "reinforced_alloy_ingot", and "aluminum_ingot" instead of "aluminium_ingot").
Punctuation is either omitted or replaced with letters where applicable (e.g. "blistering_ingot_33pc" avoids using % signs and brackets).
Roman numerals are written in Arabic (e.g. "carbon_press_2" instead of "carbon_press_ii").
If you are unsure of an item name, check *crafting.sf*.

Save *input.sf*, and then run *calculator.py*. The program will first output to the console a list of raw materials needed to build the specified items, followed by a blank line. It will then print a list of all intermediary items that must be crafted, in order. Note that this does not provide the exact recipe for any given item, nor the machine that must be used to make it.

## Adding to the recipes list
*crafting.sf* contains all the recipes. I have written about 200 to this file, as and when I've needed them; there are obviously far more than this in the whole of SlimeFun, and so you may need to add more. In this file, the product item (with a quantity) is listed at the start of each line, followed by its ingredients (also with quantities); all terms are delimited with spaces. For example, the crafting recipe for optic cable is:
> `16*optic_cable 6*optic_glass 2*copper_wire 1*synthetic_emerald_shard`

As before, all quantities (including for the product) must be listed even when equal to 1.

The *crafting.sf* file contains a number of lines featuring a product and no recipe, such as:

> `1*iron_dust`
> 
> `1*iron_ingot`
> 
> `1*iron_nugget`

These are treated as raw materials, and the program will make no further attempt to find recipes for them. All vanilla items are raw materials, as are some basic SlimeFun resources. The listed quantity for a raw material should always be 1.

If the program fails to find a required item in *crafting.sf* (listed either as a crafting recipe or a raw material), it will quit with an error message detailing the missing data.

The program does not require the individual ingredient lists or the file as a whole to be in any particular order; however, it is recommended to keep the file in alphabetical order by product for ease of maintenance.

## Custom raw materials
If you already have a production line for a certain item (or at least a large existing supply of it), you may find it unnecessary to craft any more. This is the purpose of the *custombase.sf* file.

Each line of this file should contain the name of exactly one item (WITHOUT quantities). All items listed in this file will be treated as raw materials, and the program will make no attempt to break down their crafting recipes any further.

## Syntax highlighting
Included in the repo is a *slimefun.tmbundle* folder. This can be installed into some text editors such as TextMate and PyCharm to enable custom syntax highlighting for .sf files; this is particularly useful when editing *crafting.sf*, as it marks crafting products, crafting ingredients, raw materials and quantities in different colours for ease of navigation and use.

Note that this is based on simple line-by-line regexes, and will not recognise if you refer to an item with no recipe, misspell a word, or make any other logical errors.
