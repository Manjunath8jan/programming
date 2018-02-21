Array.matrix=function(numrows, numcols){
	let arr=[];
	for(let i=0;i< numrows;++i){
		let columns=[];
		for(let j=0;j<numcols;++j){
			columns[j]=prompt();
		}
		arr[i]=columns;
	}
	return arr;
}

let tarray=Array.matrix(1,2);
