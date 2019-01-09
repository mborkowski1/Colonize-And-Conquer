//alert("zaladowalo");
var cityListNamesq = [];
var cityListXq = [];
var cityListYq = [];
var cityListOwnerNamesq = [];
var game = new Phaser.Game(1155, 800, Phaser.CANVAS, 'worldMapDiv', { preload: preload, create: create, update: update, render: render });

function preload() {
    game.load.image('backgroundMap', backgroundMap); // ready
	game.load.image('cityIcon5', cityIcon5); // ready
	game.load.image('cityIcon4', cityIcon4); // ready
	game.load.image('cityIcon3', cityIcon3); // ready
	game.load.image('cityIcon2', cityIcon2); // ready
	game.load.image('cityIcon1', cityIcon1); // ready
	game.load.image('infoPanel', infoPanel); // ready
	game.load.atlasJSONHash('tankGif', tankGif, tankGif_rules); // ready
	game.load.atlasJSONHash('tankGifS', tankGifS, tankGifS_rules); // ready
    cityListNamesq = cityListNames;
    cityListOwnerNamesq = cityListOwnerNames;
    cityListXq = cityListX;
    cityListYq = cityListY;

    liczbaMiast = cityListNamesq.length;
}

var cursors;
var x = 200;
var y = 200;
var pos_x = 450;
var pos_y = 450;
var city_list = [];
var cityListInfo = [];

var armyList = [];
var armyListS = [];
var infoPanel;
var text;
var liczbaMiast = 0;
var lineList = [];
var graphics = [];

var lineListS = [];
var graphicsS = [];

class cityInfoPanelClass{
	constructor(x, y, nazwaWioski, wlasciciel, punkty, id) {
		this.x = x;
		this.y = y;
		this.nazwaWioski = nazwaWioski;
		this.wlasciciel = wlasciciel;
		this.punkty = punkty;
		this.id = id;
		if(punkty > 3999){
			this.cityIcon = "cityIcon5";
		}
		if(punkty>2999 && punkty < 4000){
			this.cityIcon = "cityIcon4";
		}
		if(punkty>1999 && punkty < 3000){
			this.cityIcon = "cityIcon3";
		}
		if(punkty>999 && punkty < 2000){
			this.cityIcon = "cityIcon2";
		}
		if(punkty < 1000){
			this.cityIcon = "cityIcon1";
		}
		this.sprite = game.add.sprite(this.x, this.y, this.cityIcon);
	}
	sayHi() {
		alert(this.nazwaWioski);
	}
}

function create() {
    game.physics.startSystem(Phaser.Physics.ARCADE);

	game.world.setBounds(-0, -0, 3200, 2400);

	game.add.sprite(0, 0, 'backgroundMap');
	text = game.add.text(50, 0, '', { font:"10px Arial", fill: 'black' });


	for(var i=0; i<liczbaMiast;i++){
		cityListInfo[i] = new cityInfoPanelClass(parseInt(cityListXq[i]), parseInt(cityListYq[i]), cityListNamesq[i], cityListOwnerNamesq[i], parseInt(cityListPoints[i]), parseInt(cityListId[i]));
		cityListInfo[i].sprite.events.onInputOver.add(listenerOverCity, this, 0, cityListInfo[i].x, cityListInfo[i].y, cityListInfo[i].nazwaWioski, cityListInfo[i].wlasciciel, cityListInfo[i].punkty);
		cityListInfo[i].sprite.events.onInputOut.add(listenerOverCityDelete);
		cityListInfo[i].sprite.events.onInputDown.add(listenerClickCity, this, 0, cityListId[i]);
		cityListInfo[i].sprite.inputEnabled = true;
	}

	for(var i=0;i<liczbaArmi;i++){
        lineList[i] = new Phaser.Line(parseInt(cityListAttackerX[i])+25, parseInt(cityListAttackerY[i])+25, parseInt(cityListDefenderX[i])+25, parseInt(cityListDefenderY[i])+25);

        graphics[i]=game.add.graphics(0,0);
        graphics[i].lineStyle(5, 0xffd900, 1);
        graphics[i].moveTo(lineList[i].start.x,lineList[i].start.y);
        graphics[i].lineTo(lineList[i].end.x,lineList[i].end.y);
        graphics[i].endFill();

        //////
        current_x = parseInt(cityListAttackerX[i]);
        current_y = parseInt(cityListAttackerY[i]);
        send_time = cityListAttackerTime[i];
        arrive_time = cityLisDefenderTime[i];
        current_time = Date.now() / 1000;
        //////
        travel_time = Math.abs(send_time - arrive_time);
        traveled_time = Math.abs(arrive_time - current_time);
        percent_traveled = 100 * traveled_time / travel_time;
        percent_traveled = (100 - percent_traveled) / 100;
        current_x = (parseInt(cityListDefenderX[i]) - current_x) * percent_traveled;
        current_x = parseInt(cityListAttackerX[i]) + current_x;
        current_y = (parseInt(cityListDefenderY[i]) - current_y) * percent_traveled;
        current_y = parseInt(cityListAttackerY[i]) + current_y;
        //////

        armyList[i] = game.add.sprite(current_x, current_y, 'tankGif');

        game.time.events.add(Phaser.Timer.SECOND * (cityLisDefenderTime[i] - (Date.now() / 1000)), stopAnimation, this, armyList[i]);
        game.time.events.add(Phaser.Timer.SECOND * (cityLisDefenderTime[i] - (Date.now() / 1000)), stopLine, this, graphics[i]);

        armyList[i].animations.add('run');
        armyList[i].animations.play('run', 15, true);
        game.physics.arcade.enable(armyList[i]);

        game.physics.arcade.moveToXY(armyList[i], parseInt(cityListDefenderX[i]), parseInt(cityListDefenderY[i]), 10, (cityLisDefenderTime[i] - (Date.now() / 1000))*1000);
    }

    for(var i=0;i<liczbaArmiS;i++){
        lineListS[i] = new Phaser.Line(parseInt(cityListAttackerXS[i])+25, parseInt(cityListAttackerYS[i])+25, parseInt(cityListDefenderXS[i])+25, parseInt(cityListDefenderYS[i])+25);

        graphicsS[i]=game.add.graphics(0,0);
        graphicsS[i].lineStyle(5, 0xffd900, 1);
        graphicsS[i].moveTo(lineListS[i].start.x,lineListS[i].start.y);
        graphicsS[i].lineTo(lineListS[i].end.x,lineListS[i].end.y);
        graphicsS[i].endFill();

        //////
        current_x = parseInt(cityListAttackerXS[i]);
        current_y = parseInt(cityListAttackerYS[i]);
        send_time = cityListAttackerTimeS[i];
        arrive_time = cityLisDefenderTimeS[i];
        current_time = Date.now() / 1000;
        //////
        travel_time = Math.abs(send_time - arrive_time);
        traveled_time = Math.abs(arrive_time - current_time);
        percent_traveled = 100 * traveled_time / travel_time;
        percent_traveled = (100 - percent_traveled) / 100;
        current_x = (parseInt(cityListDefenderXS[i]) - current_x) * percent_traveled;
        current_x = parseInt(cityListAttackerXS[i]) + current_x;
        current_y = (parseInt(cityListDefenderYS[i]) - current_y) * percent_traveled;
        current_y = parseInt(cityListAttackerYS[i]) + current_y;
        //////

        armyListS[i] = game.add.sprite(current_x, current_y, 'tankGifS');

        game.time.events.add(Phaser.Timer.SECOND * (cityLisDefenderTimeS[i] - (Date.now() / 1000)), stopAnimation, this, armyListS[i]);
        game.time.events.add(Phaser.Timer.SECOND * (cityLisDefenderTimeS[i] - (Date.now() / 1000)), stopLine, this, graphicsS[i]);

        armyListS[i].animations.add('run');
        armyListS[i].animations.play('run', 15, true);
        game.physics.arcade.enable(armyListS[i]);

        game.physics.arcade.moveToXY(armyListS[i], parseInt(cityListDefenderXS[i]), parseInt(cityListDefenderYS[i]), 10, (cityLisDefenderTimeS[i] - (Date.now() / 1000))*1000);
    }

    cursors = game.input.keyboard.createCursorKeys();
}

function stopLine(i) {
    i.destroy();
    //alert("One of your army arrived at destination");
}

function stopAnimation(i) {
    i.destroy();
    //alert("One of your army arrived at destination");
}

function listenerClickCity(one, two, idOfCity) {
    window.location.href = idOfCity;
}

function listenerOverCity(one, two, xx, yy, nazwaWioski, wlasciciel, punkty) {
	infoPanel = game.add.sprite(xx+50, yy, 'infoPanel');
	text = game.add.text(xx+50, yy, '', { font:"10px Arial", fill: 'black' });
    text.text = "Nazwa wioski: " + nazwaWioski + "\nWlasciciel: " + wlasciciel + "\npunkty: " + punkty + "\npoz X: " + xx + "\npoz Y: " + yy;
}

function listenerOverCityDelete() {
    text.text="";
	infoPanel.destroy();
}

function update() {
	
	if (this.game.input.activePointer.isDown) {	
		if (this.game.origDragPoint) {			
			this.game.camera.x += this.game.origDragPoint.x - this.game.input.activePointer.position.x;		
			this.game.camera.y += this.game.origDragPoint.y - this.game.input.activePointer.position.y;	
		}
		this.game.origDragPoint = this.game.input.activePointer.position.clone();
	}
	else {	
		this.game.origDragPoint = null;
	}
	
    if (cursors.up.isDown)
    {
        game.camera.y -= 4;
    }
    else if (cursors.down.isDown)
    {
        game.camera.y += 4;
    }

    if (cursors.left.isDown)
    {
        game.camera.x -= 4;
    }
    else if (cursors.right.isDown)
    {
        game.camera.x += 4;
    }

}

function render() {

}
