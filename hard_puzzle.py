pazl = ['v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15',\
	'v16', 'v17', 'v18', 'v19', 'v20', 'v21', 'v22', 'v23', 'v24', 'v25', 'v26', 'v27', 'v28', 'v29', 'v30',\
	'v31', 'v32', 'v33', 'v34', 'v35', 'v36', 'v37', 'v38', 'v39', 'v40', 'v41', 'v42', 'v43', 'v44', 'v45',\
	'v46', 'v47', 'v48', 'v49', 'v50', 'v51', 'v52', 'v53', 'v54', 'v55', 'v56', 'v57', 'v58', 'v59', 'v60',\
	'v61', 'v62', 'v63', 'v64', 'v65', 'v66', 'v67', 'v68', 'v69', 'v70', 'v71', 'v72', 'v73', 'v74', 'v75',\
	'v76', 'v77', 'v78', 'v79', 'v80', 'v81', 'v82', 'v83', 'v84', 'v85', 'v86', 'v87', 'v88', 'v89', 'v90',\
	'v91', 'v92', 'v93', 'v94', 'v95', 'v96', 'v97', 'v98', 'v99', 'v100', 'v101', 'v102', 'v103', 'v104', 'v105',\
	'v106', 'v107', 'v108', 'v109', 'v110', 'v111', 'v112', 'v113', 'v114', 'v115', 'v116', 'v117', 'v118', 'v119', 'v120',\
	'v121', 'v122']
domains = {pazl[0]:[1,2,3,4,5,6,7,8,9],pazl[1]:[1,2,3,4,5,6,7,8,9],pazl[2]:[1,2,3,4,5,6,7,8,9],\
	pazl[3]:[1,2,3,4,5,6,7,8,9],pazl[4]:[1,2,3,4,5,6,7,8,9],pazl[5]:[1,2,3,4,5,6,7,8,9],\
	pazl[6]:[1,2,3,4,5,6,7,8,9],pazl[7]:[1,2,3,4,5,6,7,8,9],pazl[8]:[1,2,3,4,5,6,7,8,9],\
	pazl[9]:[1,2,3,4,5,6,7,8,9],pazl[10]:[1,2,3,4,5,6,7,8,9],pazl[11]:[1,2,3,4,5,6,7,8,9],\
	pazl[12]:[1,2,3,4,5,6,7,8,9],pazl[13]:[1,2,3,4,5,6,7,8,9],pazl[14]:[1,2,3,4,5,6,7,8,9],\
	pazl[15]:[1,2,3,4,5,6,7,8,9],pazl[16]:[1,2,3,4,5,6,7,8,9],pazl[17]:[1,2,3,4,5,6,7,8,9],\
	pazl[18]:[1,2,3,4,5,6,7,8,9],pazl[19]:[1,2,3,4,5,6,7,8,9],pazl[20]:[1,2,3,4,5,6,7,8,9],\
	pazl[21]:[1,2,3,4,5,6,7,8,9],pazl[22]:[1,2,3,4,5,6,7,8,9],pazl[23]:[1,2,3,4,5,6,7,8,9],\
	pazl[24]:[1,2,3,4,5,6,7,8,9],pazl[25]:[1,2,3,4,5,6,7,8,9],pazl[26]:[1,2,3,4,5,6,7,8,9],\
	pazl[27]:[1,2,3,4,5,6,7,8,9],pazl[28]:[1,2,3,4,5,6,7,8,9],pazl[29]:[1,2,3,4,5,6,7,8,9],\
	pazl[30]:[1,2,3,4,5,6,7,8,9],pazl[31]:[1,2,3,4,5,6,7,8,9],pazl[32]:[1,2,3,4,5,6,7,8,9],\
	pazl[33]:[1,2,3,4,5,6,7,8,9],pazl[34]:[1,2,3,4,5,6,7,8,9],pazl[35]:[1,2,3,4,5,6,7,8,9],\
	pazl[36]:[1,2,3,4,5,6,7,8,9],pazl[37]:[1,2,3,4,5,6,7,8,9],pazl[38]:[1,2,3,4,5,6,7,8,9],\
	pazl[39]:[1,2,3,4,5,6,7,8,9],pazl[40]:[1,2,3,4,5,6,7,8,9],pazl[41]:[1,2,3,4,5,6,7,8,9],\
	pazl[42]:[1,2,3,4,5,6,7,8,9],pazl[43]:[1,2,3,4,5,6,7,8,9],pazl[44]:[1,2,3,4,5,6,7,8,9],\
	pazl[45]:[1,2,3,4,5,6,7,8,9],pazl[46]:[1,2,3,4,5,6,7,8,9],pazl[47]:[1,2,3,4,5,6,7,8,9],\
	pazl[48]:[1,2,3,4,5,6,7,8,9],pazl[49]:[1,2,3,4,5,6,7,8,9],pazl[50]:[1,2,3,4,5,6,7,8,9],\
	pazl[51]:[1,2,3,4,5,6,7,8,9],pazl[52]:[1,2,3,4,5,6,7,8,9],pazl[53]:[1,2,3,4,5,6,7,8,9],\
	pazl[54]:[1,2,3,4,5,6,7,8,9],pazl[55]:[1,2,3,4,5,6,7,8,9],pazl[56]:[1,2,3,4,5,6,7,8,9],\
	pazl[57]:[1,2,3,4,5,6,7,8,9],pazl[58]:[1,2,3,4,5,6,7,8,9],pazl[59]:[1,2,3,4,5,6,7,8,9],\
	pazl[60]:[1,2,3,4,5,6,7,8,9],pazl[61]:[1,2,3,4,5,6,7,8,9],pazl[62]:[1,2,3,4,5,6,7,8,9],\
	pazl[63]:[1,2,3,4,5,6,7,8,9],pazl[64]:[1,2,3,4,5,6,7,8,9],pazl[65]:[1,2,3,4,5,6,7,8,9],\
	pazl[66]:[1,2,3,4,5,6,7,8,9],pazl[67]:[1,2,3,4,5,6,7,8,9],pazl[68]:[1,2,3,4,5,6,7,8,9],\
	pazl[69]:[1,2,3,4,5,6,7,8,9],pazl[70]:[1,2,3,4,5,6,7,8,9],pazl[71]:[1,2,3,4,5,6,7,8,9],\
	pazl[72]:[1,2,3,4,5,6,7,8,9],pazl[73]:[1,2,3,4,5,6,7,8,9],pazl[74]:[1,2,3,4,5,6,7,8,9],\
	pazl[75]:[1,2,3,4,5,6,7,8,9],pazl[76]:[1,2,3,4,5,6,7,8,9]}
domain_c77 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			if x1 != x2 and x1 != x3 and x2 != x3 and x1+x2+x3==7:
				domain_c77.append((x1,x2,x3,('v0','v6','v14')))
domain_c78 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			if x1 != x2 and x1 != x3 and x2 != x3 and x1+x2+x3==16:
				domain_c78.append((x1,x2,x3,('v1','v7','v15')))
domain_c79 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				for x5 in range(1,10):
					for x6 in range(1,10):
						if x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x1 != x6 and x2 != x3\
						and x2 != x4 and x2 != x5 and x2 != x6 and x3 != x4 and x3 != x5 and x3 != x6\
						and x4 != x5 and x4 != x6 and x5 != x6 and x1+x2+x3+x4+x5+x6==22:
							domain_c79.append((x1,x2,x3,x4,x5,x6,('v2','v8','v17','v23','v31','v37')))
domain_c80 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==10:
			domain_c80.append((x1,x2,('v3','v9')))
domain_c81 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				for x5 in range(1,10):
					for x6 in range(1,10):
						for x7 in range(1,10):
							if x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x1 != x6 and x1 != x7 and x2 != x3\
							and x2 != x4 and x2 != x5 and x2 != x6 and x2 != x7 and x3 != x4 and x3 != x5 and x3 != x6 and x3 != x7\
							and x4 != x5 and x4 != x6 and x4 != x7 and x5 != x6 and x5 != x7 and x6 != x7 and x1+x2+x3+x4+x5+x6+x7==29:
								domain_c81.append((x1,x2,x3,x4,x5,x6,x7,('v4','v12','v20','v27','v34','v40','v46')))
domain_c82 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				if x1 != x2 and x1 != x3 and x1 != x4 and x2 != x3 and x2 != x4 and x3 != x4 and x1+x2+x3+x4==29:
					domain_c82.append((x1,x2,x3,x4,('v5','v13','v21','v28')))
domain_c83 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			if x1 != x2 and x1 != x3 and x2 != x3 and x1+x2+x3==9:
				domain_c83.append((x1,x2,x3,('v10','v18','v25')))
domain_c84 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				if x1 != x2 and x1 != x3 and x1 != x4 and x2 != x3 and x2 != x4 and x3 != x4 and x1+x2+x3+x4==13:
					domain_c84.append((x1,x2,x3,x4,('v11','v19','v26','v33')))
domain_c85 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==13:
			domain_c85.append((x1,x2,('v16','v22')))
domain_c86 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				for x5 in range(1,10):
					if x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x2 != x3 and x2 != x4\
					and x2 != x5 and x3 != x4 and x3 != x5 and x4 != x5 and x1+x2+x3+x4+x5==34:
						domain_c86.append((x1,x2,x3,x4,x5,('v24','v32','v38','v44','v52')))
domain_c87 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==11:
			domain_c87.append((x1,x2,('v29','v35')))
domain_c88 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				for x5 in range(1,10):
					for x6 in range(1,10):
						for x7 in range(1,10):
							if x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x1 != x6 and x1 != x7 and x2 != x3\
							and x2 != x4 and x2 != x5 and x2 != x6 and x2 != x7 and x3 != x4 and x3 != x5 and x3 != x6 and x3 != x7\
							and x4 != x5 and x4 != x6 and x4 != x7 and x5 != x6 and x5 != x7 and x6 != x7 and x1+x2+x3+x4+x5+x6+x7==29:
								domain_c88.append((x1,x2,x3,x4,x5,x6,x7,('v30','v36','v42','v49','v56','v64','v72')))
domain_c89 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				for x5 in range(1,10):
					for x6 in range(1,10):
						if x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x1 != x6 and x2 != x3\
						and x2 != x4 and x2 != x5 and x2 != x6 and x3 != x4 and x3 != x5 and x3 != x6\
						and x4 != x5 and x4 != x6 and x5 != x6 and x1+x2+x3+x4+x5+x6==24:
							domain_c89.append((x1,x2,x3,x4,x5,x6,('v39','v45','v53','v59','v68','v74')))
domain_c90 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==4:
			domain_c90.append((x1,x2,('v41','v47')))
domain_c91 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				if x1 != x2 and x1 != x3 and x1 != x4 and x2 != x3 and x2 != x4 and x3 != x4 and x1+x2+x3+x4==16:
					domain_c91.append((x1,x2,x3,x4,('v43','v50','v57','v65')))
domain_c92 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				if x1 != x2 and x1 != x3 and x1 != x4 and x2 != x3 and x2 != x4 and x3 != x4 and x1+x2+x3+x4==11:
					domain_c92.append((x1,x2,x3,x4,('v48','v55','v63','v71')))
domain_c93 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			if x1 != x2 and x1 != x3 and x2 != x3 and x1+x2+x3==17:
				domain_c93.append((x1,x2,x3,('v51','v58','v66')))
domain_c94 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==14:
			domain_c94.append((x1,x2,('v54','v60')))
domain_c95 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			if x1 != x2 and x1 != x3 and x2 != x3 and x1+x2+x3==10:
				domain_c95.append((x1,x2,x3,('v61','v69','v75')))
domain_c96 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			if x1 != x2 and x1 != x3 and x2 != x3 and x1+x2+x3==24:
				domain_c96.append((x1,x2,x3,('v62','v70','v76')))
domain_c97 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==16:
			domain_c97.append((x1,x2,('v67','v73')))
domain_c98 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==13:
			domain_c98.append((x1,x2,('v0','v1')))
domain_c99 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==9:
			domain_c99.append((x1,x2,('v2','v3')))
domain_c100 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==9:
			domain_c100.append((x1,x2,('v4','v5')))
domain_c101 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==4:
			domain_c101.append((x1,x2,('v6','v7')))
domain_c102 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				for x5 in range(1,10):
					for x6 in range(1,10):
						if x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x1 != x6 and x2 != x3\
						and x2 != x4 and x2 != x5 and x2 != x6 and x3 != x4 and x3 != x5 and x3 != x6\
						and x4 != x5 and x4 != x6 and x5 != x6 and x1+x2+x3+x4+x5+x6==38:
							domain_c102.append((x1,x2,x3,x4,x5,x6,('v8','v9','v10','v11','v12','v13')))
domain_c103 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				if x1 != x2 and x1 != x3 and x1 != x4 and x2 != x3 and x2 != x4 and x3 != x4 and x1+x2+x3+x4==14:
					domain_c103.append((x1,x2,x3,x4,('v14','v15','v16','v17')))
domain_c104 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				if x1 != x2 and x1 != x3 and x1 != x4 and x2 != x3 and x2 != x4 and x3 != x4 and x1+x2+x3+x4==12:
					domain_c104.append((x1,x2,x3,x4,('v18','v19','v20','v21')))
domain_c105 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				for x5 in range(1,10):
					for x6 in range(1,10):
						for x7 in range(1,10):
							if x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x1 != x6 and x1 != x7 and x2 != x3\
							and x2 != x4 and x2 != x5 and x2 != x6 and x2 != x7 and x3 != x4 and x3 != x5 and x3 != x6 and x3 != x7\
							and x4 != x5 and x4 != x6 and x4 != x7 and x5 != x6 and x5 != x7 and x6 != x7 and x1+x2+x3+x4+x5+x6+x7==31:
								domain_c105.append((x1,x2,x3,x4,x5,x6,x7,('v22','v23','v24','v25','v26','v27','v28')))
domain_c106 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==13:
			domain_c106.append((x1,x2,('v29','v30')))
domain_c107 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==16:
			domain_c107.append((x1,x2,('v31','v32')))
domain_c108 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==4:
			domain_c108.append((x1,x2,('v33','v34')))
domain_c109 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==3:
			domain_c109.append((x1,x2,('v35','v36')))
domain_c110 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			if x1 != x2 and x1 != x3 and x2 != x3 and x1+x2+x3==21:
				domain_c110.append((x1,x2,x3,('v37','v38','v39')))
domain_c111 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==8:
			domain_c111.append((x1,x2,('v40','v41')))
domain_c112 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==4:
			domain_c112.append((x1,x2,('v42','v43')))
domain_c113 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==8:
			domain_c113.append((x1,x2,('v44','v45')))
domain_c114 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==3:
			domain_c114.append((x1,x2,('v46','v47')))
domain_c115 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				for x5 in range(1,10):
					for x6 in range(1,10):
						for x7 in range(1,10):
							if x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x1 != x6 and x1 != x7 and x2 != x3\
							and x2 != x4 and x2 != x5 and x2 != x6 and x2 != x7 and x3 != x4 and x3 != x5 and x3 != x6 and x3 != x7\
							and x4 != x5 and x4 != x6 and x4 != x7 and x5 != x6 and x5 != x7 and x6 != x7 and x1+x2+x3+x4+x5+x6+x7==29:
								domain_c115.append((x1,x2,x3,x4,x5,x6,x7,('v48','v49','v50','v51','v52','v53','v54')))
domain_c116 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				if x1 != x2 and x1 != x3 and x1 != x4 and x2 != x3 and x2 != x4 and x3 != x4 and x1+x2+x3+x4==17:
					domain_c116.append((x1,x2,x3,x4,('v55','v56','v57','v58')))
domain_c117 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				if x1 != x2 and x1 != x3 and x1 != x4 and x2 != x3 and x2 != x4 and x3 != x4 and x1+x2+x3+x4==29:
					domain_c117.append((x1,x2,x3,x4,('v59','v60','v61','v62')))
domain_c118 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				for x5 in range(1,10):
					for x6 in range(1,10):
						if x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x1 != x6 and x2 != x3\
						and x2 != x4 and x2 != x5 and x2 != x6 and x3 != x4 and x3 != x5 and x3 != x6\
						and x4 != x5 and x4 != x6 and x5 != x6 and x1+x2+x3+x4+x5+x6==38:
							domain_c118.append((x1,x2,x3,x4,x5,x6,('v63','v64','v65','v66','v67','v68')))
domain_c119 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==10:
			domain_c119.append((x1,x2,('v69','v70')))
domain_c120 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==3:
			domain_c120.append((x1,x2,('v71','v72')))
domain_c121 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==13:
			domain_c121.append((x1,x2,('v73','v74')))
domain_c122 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==9:
			domain_c122.append((x1,x2,('v75','v76')))
domains.update({pazl[77]:domain_c77})
domains.update({pazl[78]:domain_c78})
domains.update({pazl[79]:domain_c79})
domains.update({pazl[80]:domain_c80})
domains.update({pazl[81]:domain_c81})
domains.update({pazl[82]:domain_c82})
domains.update({pazl[83]:domain_c83})
domains.update({pazl[84]:domain_c84})
domains.update({pazl[85]:domain_c85})
domains.update({pazl[86]:domain_c86})
domains.update({pazl[87]:domain_c87})
domains.update({pazl[88]:domain_c88})
domains.update({pazl[89]:domain_c89})
domains.update({pazl[90]:domain_c90})
domains.update({pazl[91]:domain_c91})
domains.update({pazl[92]:domain_c92})
domains.update({pazl[93]:domain_c93})
domains.update({pazl[94]:domain_c94})
domains.update({pazl[95]:domain_c95})
domains.update({pazl[96]:domain_c96})
domains.update({pazl[97]:domain_c97})
domains.update({pazl[98]:domain_c98})
domains.update({pazl[99]:domain_c99})
domains.update({pazl[100]:domain_c100})
domains.update({pazl[101]:domain_c101})
domains.update({pazl[102]:domain_c102})
domains.update({pazl[103]:domain_c103})
domains.update({pazl[104]:domain_c104})
domains.update({pazl[105]:domain_c105})
domains.update({pazl[106]:domain_c106})
domains.update({pazl[107]:domain_c107})
domains.update({pazl[108]:domain_c108})
domains.update({pazl[109]:domain_c109})
domains.update({pazl[110]:domain_c110})
domains.update({pazl[111]:domain_c111})
domains.update({pazl[112]:domain_c112})
domains.update({pazl[113]:domain_c113})
domains.update({pazl[114]:domain_c114})
domains.update({pazl[115]:domain_c115})
domains.update({pazl[116]:domain_c116})
domains.update({pazl[117]:domain_c117})
domains.update({pazl[118]:domain_c118})
domains.update({pazl[119]:domain_c119})
domains.update({pazl[120]:domain_c120})
domains.update({pazl[121]:domain_c121})
domains.update({pazl[122]:domain_c122})

neighbors = {pazl[0]:[pazl[1], pazl[6], pazl[14], pazl[77], pazl[98]],\
	pazl[1]:[pazl[0], pazl[7], pazl[15], pazl[78], pazl[98]],\
	pazl[2]:[pazl[3], pazl[8], pazl[17], pazl[23], pazl[31], pazl[37], pazl[79], pazl[99]],\
	pazl[3]:[pazl[2], pazl[9], pazl[80], pazl[99]],\
	pazl[4]:[pazl[5], pazl[12], pazl[20], pazl[27], pazl[34], pazl[40], pazl[46], pazl[81], pazl[100]],\
	pazl[5]:[pazl[4], pazl[13], pazl[21], pazl[28], pazl[82], pazl[100]],\
	pazl[6]:[pazl[7], pazl[0], pazl[14], pazl[77], pazl[101]],\
	pazl[7]:[pazl[6], pazl[1], pazl[15], pazl[78], pazl[101]],\
	pazl[8]:[pazl[9], pazl[10], pazl[11], pazl[12], pazl[13], pazl[2], pazl[17], pazl[23], pazl[31], pazl[37], pazl[79], pazl[102]],\
	pazl[9]:[pazl[3], pazl[8], pazl[10], pazl[11], pazl[12], pazl[13], pazl[80], pazl[102]],\
	pazl[10]:[pazl[18], pazl[25], pazl[8], pazl[9], pazl[11], pazl[12], pazl[13], pazl[83], pazl[102]],\
	pazl[11]:[pazl[19], pazl[26], pazl[33], pazl[8], pazl[9], pazl[10], pazl[12], pazl[13], pazl[84], pazl[102]],\
	pazl[12]:[pazl[8], pazl[9], pazl[10], pazl[11], pazl[13], pazl[4], pazl[20], pazl[27], pazl[34], pazl[40], pazl[46], pazl[81], pazl[102]],\
	pazl[13]:[pazl[8], pazl[9], pazl[11], pazl[11], pazl[12], pazl[5], pazl[21], pazl[28], pazl[82], pazl[102]],\
	pazl[14]:[pazl[0], pazl[6], pazl[15], pazl[16], pazl[17], pazl[77], pazl[103]],\
	pazl[15]:[pazl[1], pazl[7], pazl[14], pazl[16], pazl[17], pazl[78], pazl[103]],\
	pazl[16]:[pazl[14], pazl[15], pazl[17], pazl[22], pazl[85], pazl[103]],\
	pazl[17]:[pazl[2], pazl[8], pazl[23], pazl[31], pazl[37], pazl[14], pazl[15], pazl[16], pazl[79], pazl[103]],\
	pazl[18]:[pazl[19], pazl[20], pazl[21], pazl[10], pazl[25], pazl[83], pazl[104]],\
	pazl[19]:[pazl[11], pazl[26], pazl[33], pazl[18], pazl[20], pazl[21], pazl[84], pazl[104]],\
	pazl[20]:[pazl[18], pazl[19], pazl[21], pazl[4], pazl[12], pazl[27], pazl[34], pazl[40], pazl[46], pazl[81], pazl[104]],\
	pazl[21]:[pazl[18], pazl[19], pazl[20], pazl[5], pazl[13], pazl[28], pazl[82], pazl[104]],\
	pazl[22]:[pazl[23], pazl[24], pazl[25], pazl[26], pazl[27], pazl[28], pazl[16], pazl[85], pazl[105]],\
	pazl[23]:[pazl[22], pazl[24], pazl[25], pazl[26], pazl[27], pazl[28], pazl[2], pazl[8], pazl[17], pazl[31], pazl[37], pazl[79], pazl[105]],\
	pazl[24]:[pazl[22], pazl[23], pazl[25], pazl[26], pazl[27], pazl[28], pazl[32], pazl[38], pazl[44], pazl[52], pazl[86], pazl[105]],\
	pazl[25]:[pazl[22], pazl[23], pazl[24], pazl[26], pazl[27], pazl[28], pazl[10], pazl[18], pazl[83], pazl[105]],\
	pazl[26]:[pazl[22], pazl[23], pazl[24], pazl[25], pazl[27], pazl[28], pazl[11], pazl[19], pazl[33], pazl[84], pazl[105]],\
	pazl[27]:[pazl[22], pazl[23], pazl[24], pazl[25], pazl[26], pazl[28], pazl[4], pazl[12], pazl[20], pazl[34], pazl[40], pazl[46], pazl[81], pazl[105]],\
	pazl[28]:[pazl[22], pazl[23], pazl[24], pazl[25], pazl[26], pazl[27], pazl[5], pazl[13], pazl[21], pazl[82], pazl[105]],\
	pazl[29]:[pazl[30], pazl[35], pazl[87], pazl[106]],\
	pazl[30]:[pazl[29], pazl[36], pazl[42], pazl[49], pazl[56], pazl[64], pazl[72], pazl[88], pazl[106]],\
	pazl[31]:[pazl[32], pazl[2], pazl[8], pazl[17], pazl[23], pazl[37], pazl[79], pazl[107]],\
	pazl[32]:[pazl[31], pazl[24], pazl[38], pazl[44], pazl[52], pazl[86], pazl[107]],\
	pazl[33]:[pazl[34], pazl[11], pazl[19], pazl[26], pazl[84], pazl[108]],\
	pazl[34]:[pazl[33], pazl[4], pazl[12], pazl[20], pazl[27], pazl[40], pazl[46], pazl[81], pazl[108]],\
	pazl[35]:[pazl[29], pazl[36], pazl[87], pazl[109]],\
	pazl[36]:[pazl[35], pazl[30], pazl[42], pazl[49], pazl[56], pazl[64], pazl[72], pazl[88], pazl[109]],\
	pazl[37]:[pazl[38], pazl[39], pazl[2], pazl[8], pazl[17], pazl[23], pazl[31], pazl[79], pazl[110]],\
	pazl[38]:[pazl[37], pazl[39], pazl[24], pazl[32], pazl[44], pazl[52], pazl[86], pazl[110]],\
	pazl[39]:[pazl[37], pazl[38], pazl[45], pazl[53], pazl[59], pazl[68], pazl[74], pazl[89], pazl[110]],\
	pazl[40]:[pazl[41], pazl[4], pazl[12], pazl[20], pazl[27], pazl[34], pazl[46], pazl[81], pazl[111]],\
	pazl[41]:[pazl[40], pazl[47], pazl[90], pazl[111]],\
	pazl[42]:[pazl[43], pazl[30], pazl[36], pazl[49], pazl[56], pazl[64], pazl[72], pazl[88], pazl[112]],\
	pazl[43]:[pazl[42], pazl[50], pazl[57], pazl[65], pazl[91], pazl[112]],\
	pazl[44]:[pazl[45], pazl[24], pazl[32], pazl[38], pazl[52], pazl[86], pazl[113]],\
	pazl[45]:[pazl[44], pazl[39], pazl[53], pazl[59], pazl[68], pazl[74], pazl[89], pazl[113]],\
	pazl[46]:[pazl[47], pazl[4], pazl[12], pazl[20], pazl[27], pazl[34], pazl[40], pazl[81], pazl[114]],\
	pazl[47]:[pazl[41], pazl[46], pazl[90], pazl[114]],\
	pazl[48]:[pazl[49], pazl[50], pazl[51], pazl[52], pazl[53], pazl[54], pazl[55], pazl[63], pazl[71], pazl[92], pazl[115]],\
	pazl[49]:[pazl[48], pazl[50], pazl[51], pazl[52], pazl[53], pazl[54], pazl[30], pazl[36], pazl[42], pazl[56], pazl[64], pazl[72]],\
	pazl[50]:[pazl[48], pazl[49], pazl[51], pazl[52], pazl[53], pazl[54], pazl[43], pazl[57], pazl[65]],\
	pazl[51]:[pazl[48], pazl[49], pazl[50], pazl[52], pazl[53], pazl[54], pazl[58], pazl[66], pazl[93], pazl[115]],\
	pazl[52]:[pazl[48], pazl[49], pazl[50], pazl[51], pazl[53], pazl[54], pazl[24], pazl[32], pazl[38], pazl[44], pazl[86], pazl[115]],\
	pazl[53]:[pazl[48], pazl[49], pazl[50], pazl[51], pazl[52], pazl[54], pazl[39], pazl[45], pazl[59], pazl[68], pazl[74], pazl[89], pazl[115]],\
	pazl[54]:[pazl[48], pazl[49], pazl[50], pazl[51], pazl[52], pazl[53], pazl[60], pazl[94], pazl[115]],\
	pazl[55]:[pazl[48], pazl[63], pazl[71], pazl[56], pazl[57], pazl[58], pazl[92], pazl[116]],\
	pazl[56]:[pazl[55], pazl[57], pazl[58], pazl[30], pazl[36], pazl[42], pazl[49], pazl[64], pazl[72], pazl[88], pazl[116]],\
	pazl[57]:[pazl[55], pazl[56], pazl[58], pazl[43], pazl[60], pazl[65], pazl[91], pazl[116]],\
	pazl[58]:[pazl[55], pazl[56], pazl[57], pazl[51], pazl[66], pazl[93], pazl[116]],\
	pazl[59]:[pazl[60], pazl[61], pazl[62], pazl[39], pazl[45], pazl[53], pazl[68], pazl[74], pazl[89], pazl[117]],\
	pazl[60]:[pazl[54], pazl[59], pazl[61], pazl[62], pazl[94], pazl[117]],\
	pazl[61]:[pazl[69], pazl[75], pazl[59], pazl[60], pazl[62], pazl[95], pazl[117]],\
	pazl[62]:[pazl[70], pazl[76], pazl[59], pazl[60], pazl[61], pazl[96], pazl[117]],\
	pazl[63]:[pazl[64], pazl[65], pazl[66], pazl[67], pazl[68], pazl[48], pazl[55], pazl[71], pazl[92], pazl[118]],\
	pazl[64]:[pazl[63], pazl[65], pazl[66], pazl[67], pazl[68], pazl[30], pazl[36], pazl[42], pazl[49], pazl[56], pazl[72], pazl[88], pazl[118]],\
	pazl[65]:[pazl[43], pazl[50], pazl[57], pazl[63], pazl[64], pazl[66], pazl[67], pazl[68], pazl[91], pazl[118]],\
	pazl[66]:[pazl[63], pazl[64], pazl[65], pazl[67], pazl[68], pazl[51], pazl[58], pazl[93], pazl[118]],\
	pazl[67]:[pazl[63], pazl[64], pazl[65], pazl[66], pazl[68], pazl[73], pazl[97], pazl[118]],\
	pazl[68]:[pazl[63], pazl[64], pazl[65], pazl[66], pazl[67], pazl[39], pazl[45], pazl[53], pazl[59], pazl[74], pazl[89], pazl[118]],\
	pazl[69]:[pazl[70], pazl[61], pazl[75], pazl[95], pazl[119]],\
	pazl[70]:[pazl[69], pazl[62], pazl[76], pazl[96], pazl[119]],\
	pazl[71]:[pazl[72], pazl[48], pazl[55], pazl[63], pazl[92], pazl[120]],\
	pazl[72]:[pazl[71], pazl[30], pazl[36], pazl[42], pazl[49], pazl[56], pazl[64], pazl[88], pazl[120]],\
	pazl[73]:[pazl[74], pazl[67], pazl[97], pazl[121]],\
	pazl[74]:[pazl[73], pazl[39], pazl[45], pazl[53], pazl[59], pazl[68], pazl[89], pazl[121]],\
	pazl[75]:[pazl[76], pazl[61], pazl[69], pazl[95], pazl[122]],\
	pazl[76]:[pazl[75], pazl[62], pazl[70], pazl[96], pazl[122]],\
	pazl[77]:[pazl[0], pazl[6], pazl[14]],\
	pazl[78]:[pazl[1], pazl[7], pazl[15]],\
	pazl[79]:[pazl[2], pazl[8], pazl[17], pazl[23], pazl[31], pazl[37]],\
	pazl[80]:[pazl[3], pazl[9]],\
	pazl[81]:[pazl[4], pazl[12], pazl[20], pazl[27], pazl[34], pazl[40], pazl[46]],\
	pazl[82]:[pazl[5], pazl[13], pazl[21], pazl[28]],\
	pazl[83]:[pazl[10], pazl[18], pazl[25]],\
	pazl[84]:[pazl[11], pazl[19], pazl[26], pazl[33]],\
	pazl[85]:[pazl[16], pazl[22]],\
	pazl[86]:[pazl[24], pazl[32], pazl[38], pazl[44], pazl[52]],\
	pazl[87]:[pazl[29], pazl[35]],\
	pazl[88]:[pazl[30], pazl[36], pazl[42], pazl[49], pazl[56], pazl[64], pazl[72]],\
	pazl[89]:[pazl[39], pazl[45], pazl[53], pazl[59], pazl[68], pazl[74]],\
	pazl[90]:[pazl[41], pazl[47]],\
	pazl[91]:[pazl[43], pazl[50], pazl[57], pazl[65]],\
	pazl[92]:[pazl[48], pazl[55], pazl[63], pazl[71]],\
	pazl[93]:[pazl[51], pazl[58], pazl[66]],\
	pazl[94]:[pazl[54], pazl[60]],\
	pazl[95]:[pazl[61], pazl[69], pazl[75]],\
	pazl[96]:[pazl[62], pazl[70], pazl[76]],\
	pazl[97]:[pazl[67], pazl[73]],\
	pazl[98]:[pazl[0], pazl[1]],\
	pazl[99]:[pazl[2], pazl[3]],\
	pazl[100]:[pazl[4], pazl[5]],\
	pazl[101]:[pazl[6], pazl[7]],\
	pazl[102]:[pazl[8], pazl[9], pazl[10], pazl[11], pazl[12], pazl[13]],\
	pazl[103]:[pazl[14], pazl[15], pazl[16], pazl[17]],\
	pazl[104]:[pazl[18], pazl[19], pazl[20], pazl[21]],\
	pazl[105]:[pazl[22], pazl[23], pazl[24], pazl[25], pazl[26], pazl[27], pazl[28]],\
	pazl[106]:[pazl[29], pazl[30]],\
	pazl[107]:[pazl[31], pazl[32]],\
	pazl[108]:[pazl[33], pazl[34]],\
	pazl[109]:[pazl[35], pazl[36]],\
	pazl[110]:[pazl[37], pazl[38], pazl[39]],\
	pazl[111]:[pazl[40], pazl[41]],\
	pazl[112]:[pazl[42], pazl[43]],\
	pazl[113]:[pazl[44], pazl[45]],\
	pazl[114]:[pazl[46], pazl[47]],\
	pazl[115]:[pazl[48], pazl[49], pazl[50], pazl[51], pazl[52], pazl[53], pazl[54]],\
	pazl[116]:[pazl[55], pazl[56], pazl[57], pazl[58]],\
	pazl[117]:[pazl[59], pazl[60], pazl[61], pazl[62]],\
	pazl[118]:[pazl[63], pazl[64], pazl[65], pazl[66], pazl[67], pazl[68]],\
	pazl[119]:[pazl[69], pazl[70]],\
	pazl[120]:[pazl[71], pazl[72]],\
	pazl[121]:[pazl[73], pazl[74]],\
	pazl[122]:[pazl[75], pazl[76]]}