var HIDDEN_CLASS_NAME = 'hidden'
var TARGET_CLASS_NAME = 'target'
var SOURCE_CLASS_NAME = 'source'

var targetIdToShow = 1

function main1() {
	var targets = getElements(TARGET_CLASS_NAME)
	var sources = getElements(SOURCE_CLASS_NAME)
	sources.forEach(function (sourceNode) {
		var sourceNodeId = extractId(sourceNode, SOURCE_CLASS_NAME)
		sourceNode.addEventListener('click', function () {
			showTarget(targets, sourceNodeId)
		})
	})
	showTarget(targets, targetIdToShow)
}

function getElements(type) {
	return [].slice.call(document.querySelectorAll('.' + type)).sort(function (targetNode1, targetNode2) {
		var target1Num = extractId(targetNode1, TARGET_CLASS_NAME)
		var target2Num = extractId(targetNode2, TARGET_CLASS_NAME)
		return target1Num > target2Num
	})
}

function extractId(targetNode, baseClass) {
	var currentClassIndex = targetNode.classList.length
	while (currentClassIndex--) {
		var currentClass = targetNode.classList.item(currentClassIndex)
		var maybeIdNum = parseInt(currentClass.split('-')[1])
		if (isNaN(maybeIdNum)) {
			continue
		}
		var classStrinToValidate = baseClass + '-' + maybeIdNum
		if (classStrinToValidate === currentClass) {
			return maybeIdNum
		}
	}
}

function showTarget(targets, targetId) {
	targets.forEach(function (targetNode, targetIndex) {
    var currentTargetNodeId = extractId(targetNode, TARGET_CLASS_NAME)
		if (currentTargetNodeId === targetId) {
			targetNode.classList.remove(HIDDEN_CLASS_NAME)
		} else {
			targetNode.classList.add(HIDDEN_CLASS_NAME)
		}
	})
}

main1()

function toggleText(){
    var x = document.getElementById("profiles");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }

async function get_info_Bogdan(){
	let path = "data/Users/Bogdan.xlsx"

	let res = await eel.get_user_info(path)();
	document.getElementById("res-Bogdan").innerHTML = res;
}

async function get_info_Maxim(){
	let path = "data/Users/Maxim.xlsx"

	let res = await eel.get_user_info(path)();
	document.getElementById("res-Maxim").innerHTML = res;
}

async function get_info_Oleg(){
	let path = "data/Users/Oleg.xlsx"

	let res = await eel.get_user_info(path)();
	document.getElementById("res-Oleg").innerHTML = res;
}

async function get_info_Pavel(){
	let path = "data/Users/Pavel.xlsx"

	let res = await eel.get_user_info(path)();
	document.getElementById("res-Pavel").innerHTML = res;
}

async function get_info_Vlad(){
	let path = "data/Users/Vlad.xlsx"

	let res = await eel.get_user_info(path)();
	document.getElementById("res-Vlad").innerHTML = res;
}

async function replace_info_Bogdan(){

	let path = "data/Users/Bogdan.xlsx"
	let day = document.getElementById("input-1")
	let device = document.getElementById("input-2")
	let hour = document.getElementById("input-3")

	await eel.replace_info(path, day, device, hour)();
}

async function replace_info_Maxim(){

	let path = "data/Users/Maxim.xlsx"
	let day = document.getElementById("input-1")
	let device = document.getElementById("input-2")
	let hour = document.getElementById("input-3")

	await eel.replace_info(path, day, device, hour)();
}

async function replace_info_Oleg(){

	let path = "data/Users/Oleg.xlsx"
	let day = document.getElementById("input-1")
	let device = document.getElementById("input-2")
	let hour = document.getElementById("input-3")

	await eel.replace_info(path, day, device, hour)();
}

async function replace_info_Pavel(){

	let path = "data/Users/Pavel.xlsx"
	let day = document.getElementById("input-1")
	let device = document.getElementById("input-2")
	let hour = document.getElementById("input-3")

	await eel.replace_info(path, day, device, hour)();
}

async function replace_info_Vlad(){

	let path = "data/Users/Vlad.xlsx"
	let day = document.getElementById("input-1")
	let device = document.getElementById("input-2")
	let hour = document.getElementById("input-3")

	let res = await eel.replace_info(path, day, device, hour)();
}

  async function get_all_info(){
	let t = 1;
	let res = await eel.main()();

	document.getElementById("text-all-info").innerHTML = res;

	var x = document.getElementById("block-all-info");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
}