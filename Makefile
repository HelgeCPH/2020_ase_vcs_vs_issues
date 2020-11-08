.SILENT:


GSE_Branching_vs_Quality.html:GSE_Branching_vs_Quality.md
	jupytext --to notebook GSE_Branching_vs_Quality.md
	jupyter nbconvert GSE_Branching_vs_Quality.ipynb --to html
	open GSE_Branching_vs_Quality.html