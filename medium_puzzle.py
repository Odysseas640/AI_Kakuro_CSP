medium_pazl = ['v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15',\
	'v16', 'v17', 'v18', 'v19', 'v20', 'v21', 'v22', 'v23', 'v24', 'v25', 'v26', 'v27', 'v28', 'v29', 'v30',\
	'v31', 'v32', 'v33', 'v34', 'v35', 'v36', 'v37', 'v38', 'v39', 'v40', 'v41', 'v42', 'v43', 'v44', 'v45',\
	'v46', 'v47', 'v48', 'v49', 'v50', 'v51'\
	]
domains_medium = {medium_pazl[0]:[1,2,3,4,5,6,7,8,9],medium_pazl[1]:[1,2,3,4,5,6,7,8,9],medium_pazl[2]:[1,2,3,4,5,6,7,8,9],\
	medium_pazl[3]:[1,2,3,4,5,6,7,8,9],medium_pazl[4]:[1,2,3,4,5,6,7,8,9],medium_pazl[5]:[1,2,3,4,5,6,7,8,9],\
	medium_pazl[6]:[1,2,3,4,5,6,7,8,9],medium_pazl[7]:[1,2,3,4,5,6,7,8,9],medium_pazl[8]:[1,2,3,4,5,6,7,8,9],\
	medium_pazl[9]:[1,2,3,4,5,6,7,8,9],medium_pazl[10]:[1,2,3,4,5,6,7,8,9],medium_pazl[11]:[1,2,3,4,5,6,7,8,9],\
	medium_pazl[12]:[1,2,3,4,5,6,7,8,9],medium_pazl[13]:[1,2,3,4,5,6,7,8,9],medium_pazl[14]:[1,2,3,4,5,6,7,8,9],\
	medium_pazl[15]:[1,2,3,4,5,6,7,8,9],medium_pazl[16]:[1,2,3,4,5,6,7,8,9],medium_pazl[17]:[1,2,3,4,5,6,7,8,9],\
	medium_pazl[18]:[1,2,3,4,5,6,7,8,9],medium_pazl[19]:[1,2,3,4,5,6,7,8,9],medium_pazl[20]:[1,2,3,4,5,6,7,8,9],\
	medium_pazl[21]:[1,2,3,4,5,6,7,8,9],medium_pazl[22]:[1,2,3,4,5,6,7,8,9],medium_pazl[23]:[1,2,3,4,5,6,7,8,9],\
	medium_pazl[24]:[1,2,3,4,5,6,7,8,9],medium_pazl[25]:[1,2,3,4,5,6,7,8,9],medium_pazl[26]:[1,2,3,4,5,6,7,8,9],\
	medium_pazl[27]:[1,2,3,4,5,6,7,8,9],medium_pazl[28]:[1,2,3,4,5,6,7,8,9],medium_pazl[29]:[1,2,3,4,5,6,7,8,9],\
	medium_pazl[30]:[1,2,3,4,5,6,7,8,9]}
domain_c31 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==11:
			domain_c31.append((x1,x2,('v0','v3')))
domain_c32 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==8:
			domain_c32.append((x1,x2,('v1','v4')))
domain_c33 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==15:
			domain_c33.append((x1,x2,('v2','v5')))
domain_c34 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==10:
			domain_c34.append((x1,x2,('v6','v9')))
domain_c35 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			if x1 != x2 and x1 != x3 and x2 != x3 and x1+x2+x3==7:
				domain_c35.append((x1,x2,x3,('v7','v10','v15')))
domain_c36 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				for x5 in range(1,10):
					if x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x2 != x3 and x2 != x4\
					and x2 != x5 and x3 != x4 and x3 != x5 and x4 != x5 and x1+x2+x3+x4+x5==29:
						domain_c36.append((x1,x2,x3,x4,x5,('v8','v11','v16','v20','v27')))
domain_c37 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			if x1 != x2 and x1 != x3 and x2 != x3 and x1+x2+x3==11:
				domain_c37.append((x1,x2,x3,('v12','v17','v21')))
domain_c38 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			if x1 != x2 and x1 != x3 and x2 != x3 and x1+x2+x3==19:
				domain_c38.append((x1,x2,x3,('v13','v18','v22')))
domain_c39 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			if x1 != x2 and x1 != x3 and x2 != x3 and x1+x2+x3==23:
				domain_c39.append((x1,x2,x3,('v14','v19','v23')))
domain_c40 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==4:
			domain_c40.append((x1,x2,('v24','v28')))
domain_c41 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==8:
			domain_c41.append((x1,x2,('v25','v29')))
domain_c42 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==11:
			domain_c42.append((x1,x2,('v26','v30')))
domain_c43 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			if x1 != x2 and x1 != x3 and x2 != x3 and x1+x2+x3==24:
				domain_c43.append((x1,x2,x3,('v0','v1','v2')))
domain_c44 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				for x5 in range(1,10):
					for x6 in range(1,10):
						if x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x1 != x6 and x2 != x3\
						and x2 != x4 and x2 != x5 and x2 != x6 and x3 != x4 and x3 != x5 and x3 != x6\
						and x4 != x5 and x4 != x6 and x5 != x6 and x1+x2+x3+x4+x5+x6==27:
							domain_c44.append((x1,x2,x3,x4,x5,x6,('v3','v4','v5','v6','v7','v8')))
domain_c45 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				if x1 != x2 and x1 != x3 and x1 != x4 and x2 != x3 and x2 != x4 and x3 != x4 and x1+x2+x3+x4==12:
					domain_c45.append((x1,x2,x3,x4,('v9','v10','v11','v12')))
domain_c46 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==16:
			domain_c46.append((x1,x2,('v13','v14')))
domain_c47 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			if x1 != x2 and x1 != x3 and x2 != x3 and x1+x2+x3==20:
				domain_c47.append((x1,x2,x3,('v15','v16','v17')))
domain_c48 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==17:
			domain_c48.append((x1,x2,('v18','v19')))
domain_c49 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		if x1 != x2 and x1+x2==3:
			domain_c49.append((x1,x2,('v20','v21')))
domain_c50 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			for x4 in range(1,10):
				for x5 in range(1,10):
					for x6 in range(1,10):
						if x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x1 != x6 and x2 != x3\
						and x2 != x4 and x2 != x5 and x2 != x6 and x3 != x4 and x3 != x5 and x3 != x6\
						and x4 != x5 and x4 != x6 and x5 != x6 and x1+x2+x3+x4+x5+x6==21:
							domain_c50.append((x1,x2,x3,x4,x5,x6,('v22','v23','v24','v25','v26','v27')))
domain_c51 = []
for x1 in range(1,10):
	for x2 in range(1,10):
		for x3 in range(1,10):
			if x1 != x2 and x1 != x3 and x2 != x3 and x1+x2+x3==16:
				domain_c51.append((x1,x2,x3,('v28','v29','v30')))
domains_medium.update({medium_pazl[31]:domain_c31})
domains_medium.update({medium_pazl[32]:domain_c32})
domains_medium.update({medium_pazl[33]:domain_c33})
domains_medium.update({medium_pazl[34]:domain_c34})
domains_medium.update({medium_pazl[35]:domain_c35})
domains_medium.update({medium_pazl[36]:domain_c36})
domains_medium.update({medium_pazl[37]:domain_c37})
domains_medium.update({medium_pazl[38]:domain_c38})
domains_medium.update({medium_pazl[39]:domain_c39})
domains_medium.update({medium_pazl[40]:domain_c40})
domains_medium.update({medium_pazl[41]:domain_c41})
domains_medium.update({medium_pazl[42]:domain_c42})
domains_medium.update({medium_pazl[43]:domain_c43})
domains_medium.update({medium_pazl[44]:domain_c44})
domains_medium.update({medium_pazl[45]:domain_c45})
domains_medium.update({medium_pazl[46]:domain_c46})
domains_medium.update({medium_pazl[47]:domain_c47})
domains_medium.update({medium_pazl[48]:domain_c48})
domains_medium.update({medium_pazl[49]:domain_c49})
domains_medium.update({medium_pazl[50]:domain_c50})
domains_medium.update({medium_pazl[51]:domain_c51})

neighbors_medium = {medium_pazl[0]:[medium_pazl[1], medium_pazl[2], medium_pazl[3], medium_pazl[31], medium_pazl[43]],\
	medium_pazl[1]:[medium_pazl[0], medium_pazl[2], medium_pazl[4], medium_pazl[32], medium_pazl[43]],\
	medium_pazl[2]:[medium_pazl[0], medium_pazl[1], medium_pazl[5], medium_pazl[33], medium_pazl[43]],\
	medium_pazl[3]:[medium_pazl[0], medium_pazl[4], medium_pazl[5], medium_pazl[6], medium_pazl[7], medium_pazl[8], medium_pazl[31], medium_pazl[44]],\
	medium_pazl[4]:[medium_pazl[1], medium_pazl[3], medium_pazl[5], medium_pazl[6], medium_pazl[7], medium_pazl[8], medium_pazl[32], medium_pazl[44]],\
	medium_pazl[5]:[medium_pazl[2], medium_pazl[3], medium_pazl[4], medium_pazl[6], medium_pazl[7], medium_pazl[8], medium_pazl[33], medium_pazl[44]],\
	medium_pazl[6]:[medium_pazl[3], medium_pazl[4], medium_pazl[5], medium_pazl[7], medium_pazl[8], medium_pazl[9], medium_pazl[34], medium_pazl[44]],\
	medium_pazl[7]:[medium_pazl[3], medium_pazl[4], medium_pazl[5], medium_pazl[6], medium_pazl[8], medium_pazl[10], medium_pazl[15], medium_pazl[35], medium_pazl[44]],\
	medium_pazl[8]:[medium_pazl[3], medium_pazl[4], medium_pazl[5], medium_pazl[6], medium_pazl[7], medium_pazl[11], medium_pazl[16], medium_pazl[20], medium_pazl[27], medium_pazl[36], medium_pazl[44]],\
	medium_pazl[9]:[medium_pazl[10], medium_pazl[11], medium_pazl[12], medium_pazl[6], medium_pazl[34], medium_pazl[45]],\
	medium_pazl[10]:[medium_pazl[9], medium_pazl[11], medium_pazl[12], medium_pazl[7], medium_pazl[15], medium_pazl[35], medium_pazl[45]],\
	medium_pazl[11]:[medium_pazl[9], medium_pazl[10], medium_pazl[12], medium_pazl[8], medium_pazl[16], medium_pazl[20], medium_pazl[27], medium_pazl[36], medium_pazl[45]],\
	medium_pazl[12]:[medium_pazl[9], medium_pazl[10], medium_pazl[11], medium_pazl[17], medium_pazl[21], medium_pazl[37], medium_pazl[45]],\
	medium_pazl[13]:[medium_pazl[14], medium_pazl[38], medium_pazl[46]],\
	medium_pazl[14]:[medium_pazl[13], medium_pazl[39], medium_pazl[46]],\
	medium_pazl[15]:[medium_pazl[16], medium_pazl[17], medium_pazl[7], medium_pazl[10], medium_pazl[35], medium_pazl[47]],\
	medium_pazl[16]:[medium_pazl[15], medium_pazl[17], medium_pazl[8], medium_pazl[11], medium_pazl[20], medium_pazl[27], medium_pazl[36], medium_pazl[47]],\
	medium_pazl[17]:[medium_pazl[15], medium_pazl[16], medium_pazl[12], medium_pazl[21], medium_pazl[37], medium_pazl[47]],\
	medium_pazl[18]:[medium_pazl[19], medium_pazl[38], medium_pazl[48]],\
	medium_pazl[19]:[medium_pazl[18], medium_pazl[39], medium_pazl[48]],\
	medium_pazl[20]:[medium_pazl[21], medium_pazl[8], medium_pazl[11], medium_pazl[16], medium_pazl[27], medium_pazl[36], medium_pazl[49]],\
	medium_pazl[21]:[medium_pazl[20], medium_pazl[12], medium_pazl[17], medium_pazl[37], medium_pazl[49]],\
	medium_pazl[22]:[medium_pazl[23], medium_pazl[24], medium_pazl[25], medium_pazl[26], medium_pazl[27], medium_pazl[13], medium_pazl[18], medium_pazl[38], medium_pazl[50]],\
	medium_pazl[23]:[medium_pazl[22], medium_pazl[24], medium_pazl[25], medium_pazl[26], medium_pazl[27], medium_pazl[14], medium_pazl[19], medium_pazl[39], medium_pazl[50]],\
	medium_pazl[24]:[medium_pazl[22], medium_pazl[23], medium_pazl[25], medium_pazl[26], medium_pazl[27], medium_pazl[28], medium_pazl[40], medium_pazl[50]],\
	medium_pazl[25]:[medium_pazl[22], medium_pazl[23], medium_pazl[24], medium_pazl[26], medium_pazl[27], medium_pazl[29], medium_pazl[41], medium_pazl[50]],\
	medium_pazl[26]:[medium_pazl[22], medium_pazl[23], medium_pazl[24], medium_pazl[25], medium_pazl[27], medium_pazl[30], medium_pazl[42], medium_pazl[50]],\
	medium_pazl[27]:[medium_pazl[22], medium_pazl[23], medium_pazl[24], medium_pazl[25], medium_pazl[26], medium_pazl[8], medium_pazl[11], medium_pazl[16], medium_pazl[20], medium_pazl[36], medium_pazl[50]],\
	medium_pazl[28]:[medium_pazl[24], medium_pazl[29], medium_pazl[30], medium_pazl[40], medium_pazl[51]],\
	medium_pazl[29]:[medium_pazl[25], medium_pazl[28], medium_pazl[30], medium_pazl[41], medium_pazl[51]],\
	medium_pazl[30]:[medium_pazl[26], medium_pazl[28], medium_pazl[29], medium_pazl[42], medium_pazl[51]],\
	medium_pazl[31]:[medium_pazl[0], medium_pazl[3]],\
	medium_pazl[32]:[medium_pazl[1], medium_pazl[4]],\
	medium_pazl[33]:[medium_pazl[2], medium_pazl[5]],\
	medium_pazl[34]:[medium_pazl[6], medium_pazl[9]],\
	medium_pazl[35]:[medium_pazl[7], medium_pazl[10], medium_pazl[15]],\
	medium_pazl[36]:[medium_pazl[8], medium_pazl[11], medium_pazl[16], medium_pazl[20], medium_pazl[27]],\
	medium_pazl[37]:[medium_pazl[12], medium_pazl[17], medium_pazl[21]],\
	medium_pazl[38]:[medium_pazl[13], medium_pazl[18], medium_pazl[22]],\
	medium_pazl[39]:[medium_pazl[14], medium_pazl[19], medium_pazl[23]],\
	medium_pazl[40]:[medium_pazl[24], medium_pazl[28]],\
	medium_pazl[41]:[medium_pazl[25], medium_pazl[29]],\
	medium_pazl[42]:[medium_pazl[26], medium_pazl[30]],\
	medium_pazl[43]:[medium_pazl[0], medium_pazl[1], medium_pazl[2]],\
	medium_pazl[44]:[medium_pazl[3], medium_pazl[4], medium_pazl[5], medium_pazl[6], medium_pazl[7], medium_pazl[8]],\
	medium_pazl[45]:[medium_pazl[9], medium_pazl[10], medium_pazl[11], medium_pazl[12]],\
	medium_pazl[46]:[medium_pazl[13], medium_pazl[14]],\
	medium_pazl[47]:[medium_pazl[15], medium_pazl[16], medium_pazl[17]],\
	medium_pazl[48]:[medium_pazl[18], medium_pazl[19]],\
	medium_pazl[49]:[medium_pazl[20], medium_pazl[21]],\
	medium_pazl[50]:[medium_pazl[22], medium_pazl[23], medium_pazl[24], medium_pazl[25], medium_pazl[26], medium_pazl[27]],\
	medium_pazl[51]:[medium_pazl[28], medium_pazl[29], medium_pazl[30]]\
}