var cookie = document.createElement('script');
cookie.setAttribute('src','https://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.js');
document.head.appendChild(cookie);

var game = new Phaser.Game(800, 800, Phaser.CANVAS, 'techTreeRenderDiv', { preload: preload, create: create, update: update, render: render });

var infoPanel = 0;
var text = 0;

function preload() {
    game.load.image('background', background); // ready
	game.load.image('barracks_2', barracks_2); // ready
	game.load.image('energy_2', energy_2); // ready
	game.load.image('farms_2', farms_2); // ready
	game.load.image('housing_2', housing_2); // ready
	game.load.image('mine_2', mine_2); // ready
	game.load.image('roads_2', roads_2); // ready
	game.load.image('town_hall_2', town_hall_2); // ready
	game.load.image('town_hall_3', town_hall_3); // ready
	game.load.image('infoPanel', infoPanel); // ready
	game.load.image('infoPanel2', infoPanel2); // ready
}

function listenerClickTH1() {
    var csrftoken = $.cookie('csrftoken');
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		        xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	$.ajax('', {
		type: 'POST',
		data: {
	        tech: "th1"
	    }
	});
    window.location.href = "";
}

function listenerClickTH2() {
    var csrftoken = $.cookie('csrftoken');
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		        xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	$.ajax('', {
		type: 'POST',
		data: {
	        tech: "th2"
	    }
	});
    window.location.href = "";
}

function listenerClickM() {
    var csrftoken = $.cookie('csrftoken');
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		        xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	$.ajax('', {
		type: 'POST',
		data: {
	        tech: "m"
	    }
	});
    window.location.href = "";
}

function listenerClickF() {
    var csrftoken = $.cookie('csrftoken');
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		        xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	$.ajax('', {
		type: 'POST',
		data: {
	        tech: "f"
	    }
	});
    window.location.href = "";
}

function listenerClickPP() {
    var csrftoken = $.cookie('csrftoken');
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		        xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	$.ajax('', {
		type: 'POST',
		data: {
	        tech: "pp"
	    }
	});
    window.location.href = "";
}

function listenerClickR() {
    var csrftoken = $.cookie('csrftoken');
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		        xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	$.ajax('', {
		type: 'POST',
		data: {
	        tech: "r"
	    }
	});
    window.location.href = "";
}

function listenerClickH() {
    var csrftoken = $.cookie('csrftoken');
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		        xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	$.ajax('', {
		type: 'POST',
		data: {
	        tech: "h"
	    }
	});
    window.location.href = "";
}

function listenerClickB() {
    var csrftoken = $.cookie('csrftoken');
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		        xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	$.ajax('', {
		type: 'POST',
		data: {
	        tech: "b"
	    }
	});
    window.location.href = "";
}

function listenerTH1(one, two, xx, yy) {
	infoPanel = game.add.sprite(xx+50, yy, 'infoPanel');
	text = game.add.text(xx+50, yy, '', { font:"15px Arial", fill: 'black' });
    text.text = "Town Hall \nRequirements: \nTown hall lvl 10";
}

function listenerTH2(one, two, xx, yy) {
	infoPanel = game.add.sprite(xx+50, yy, 'infoPanel');
	text = game.add.text(xx+50, yy, '', { font:"15px Arial", fill: 'black' });
    text.text = "Town Hall \nRequirements: \nTown hall lvl 20";
}

function listenerM(one, two, xx, yy) {
	infoPanel = game.add.sprite(xx+50, yy, 'infoPanel2');
	text = game.add.text(xx+50, yy, '', { font:"14px Arial", fill: 'black' });
    text.text = "Mines \nRequirements: \nMines lvl 10\nTown hall lvl 10\nTown hall 1 research";
}

function listenerF(one, two, xx, yy) {
	infoPanel = game.add.sprite(xx+50, yy, 'infoPanel2');
	text = game.add.text(xx+50, yy, '', { font:"15px Arial", fill: 'black' });
    text.text = "Farms \nRequirements: \nFarm lvl 10\nTown hall lvl 10\nTown hall 1 research";
}

function listenerPP(one, two, xx, yy) {
	infoPanel = game.add.sprite(xx+50, yy, 'infoPanel2');
	text = game.add.text(xx+50, yy, '', { font:"15px Arial", fill: 'black' });
    text.text = "Power Plant \nRequirements: \nPower plant lvl 10\nTown hall lvl 20\nTown hall 1 research\nTown hall 2 research";
}

function listenerR(one, two, xx, yy) {
	infoPanel = game.add.sprite(xx+50, yy, 'infoPanel2');
	text = game.add.text(xx+50, yy, '', { font:"15px Arial", fill: 'black' });
    text.text = "Roads \nRequirements: \nRoads lvl 10\nTown hall lvl 20\nTown hall 1 research\nTown hall 2 research";
}

function listenerH(one, two, xx, yy) {
	infoPanel = game.add.sprite(xx+50, yy, 'infoPanel2');
	text = game.add.text(xx+50, yy, '', { font:"15px Arial", fill: 'black' });
    text.text = "Housing \nRequirements: \nHousing lvl 10\nTown hall lvl 20\nTown hall 1 research\nTown hall 2 research";
}

function listenerB(one, two, xx, yy) {
	infoPanel = game.add.sprite(xx+50, yy, 'infoPanel2');
	text = game.add.text(xx+50, yy, '', { font:"15px Arial", fill: 'black' });
    text.text = "Barracks \nRequirements: \nBarracks lvl 10\nTown hall lvl 20\nHousing lvl 10\nTown hall 1 research\nTown hall 2 research\nHousing research";
}

function listenerOverTech() {
    text.text="";
	infoPanel.destroy();
}

function create() {

	game.world.setBounds(-0, -0, 800, 800);
	
	game.add.sprite(0, 0, 'background');

    var graphics = game.add.graphics(345, 45);

    var line1 = new Phaser.Line(440, 85, 200, 220);
    graphics=game.add.graphics(0,0);
    graphics.lineStyle(15, 0xffd900, 1);
    graphics.moveTo(line1.start.x,line1.start.y);
    graphics.lineTo(line1.end.x,line1.end.y);
    graphics.endFill();

    line1 = new Phaser.Line(440, 105, 650, 220);
    graphics=game.add.graphics(0,0);
    graphics.lineStyle(15, 0xffd900, 1);
    graphics.moveTo(line1.start.x,line1.start.y);
    graphics.lineTo(line1.end.x,line1.end.y);
    graphics.endFill();

    var line1 = new Phaser.Line(420, 350, 200, 520);
    graphics=game.add.graphics(0,0);
    graphics.lineStyle(15, 0xffd900, 1);
    graphics.moveTo(line1.start.x,line1.start.y);
    graphics.lineTo(line1.end.x,line1.end.y);
    graphics.endFill();

    line1 = new Phaser.Line(420, 365, 650, 520);
    graphics=game.add.graphics(0,0);
    graphics.lineStyle(15, 0xffd900, 1);
    graphics.moveTo(line1.start.x,line1.start.y);
    graphics.lineTo(line1.end.x,line1.end.y);
    graphics.endFill();

    line1 = new Phaser.Line(420, 80, 420, 350);
    graphics=game.add.graphics(0,0);
    graphics.lineStyle(15, 0xffd900, 1);
    graphics.moveTo(line1.start.x,line1.start.y);
    graphics.lineTo(line1.end.x,line1.end.y);
    graphics.endFill();

    line1 = new Phaser.Line(420, 350, 420, 450);
    graphics=game.add.graphics(0,0);
    graphics.lineStyle(15, 0xffd900, 1);
    graphics.moveTo(line1.start.x,line1.start.y);
    graphics.lineTo(line1.end.x,line1.end.y);
    graphics.endFill();

    line1 = new Phaser.Line(420, 450, 420, 650);
    graphics=game.add.graphics(0,0);
    graphics.lineStyle(15, 0xffd900, 1);
    graphics.moveTo(line1.start.x,line1.start.y);
    graphics.lineTo(line1.end.x,line1.end.y);
    graphics.endFill();

    /////////////////// TH1
    if(researchTH1 == 1){
        graphics = game.add.graphics(345, 45);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x334CFF, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        th1 = game.add.sprite(365, 50, "town_hall_2");
        th1.scale.setTo(0.5, 0.5);
        th1.inputEnabled = true;
    }
    else if(researchTH1 == 0 && lvltownHall >= 10){
        graphics = game.add.graphics(345, 45);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x35FF08, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        th1 = game.add.sprite(365, 50, "town_hall_2");
        th1.scale.setTo(0.5, 0.5);
        th1.inputEnabled = true;
        th1.events.onInputDown.add(listenerClickTH1, this);
    }
    else{
        graphics = game.add.graphics(345, 45);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0xFF0808, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        th1 = game.add.sprite(365, 50, "town_hall_2");
        th1.scale.setTo(0.5, 0.5);
        th1.inputEnabled = true;
    }
    th1.events.onInputOver.add(listenerTH1, this, 0, th1.x, th1.y);
	th1.events.onInputOut.add(listenerOverTech);
    //////////////////////// TH2
    if(researchTH2 == 1){
        graphics = game.add.graphics(345, 295);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x334CFF, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        th2 = game.add.sprite(350, 300, "town_hall_3");
        th2.scale.setTo(0.5, 0.5);
        th2.inputEnabled = true;
    }
    else if(researchTH1 == 1 && researchTH2 == 0 && lvltownHall >= 20){
        graphics = game.add.graphics(345, 295);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x35FF08, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        th2 = game.add.sprite(350, 300, "town_hall_3");
        th2.scale.setTo(0.5, 0.5);
	    th2.inputEnabled = true;
        th2.events.onInputDown.add(listenerClickTH2, this);
    }
    else{
        graphics = game.add.graphics(345, 295);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0xFF0808, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        th2 = game.add.sprite(350, 300, "town_hall_3");
        th2.scale.setTo(0.5, 0.5);
        th2.inputEnabled = true;
    }
    th2.events.onInputOver.add(listenerTH2, this, 0, th2.x, th2.y);
	th2.events.onInputOut.add(listenerOverTech);
    ///////////////////////// M
    if(researchM == 1){
        graphics = game.add.graphics(125, 165);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x334CFF, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        m = game.add.sprite(130, 170, "mine_2");
        m.scale.setTo(0.5, 0.5);
        m.inputEnabled = true;
    }
    else if(researchTH1 == 1 && researchM == 0 && lvlmine >= 10){
        graphics = game.add.graphics(125, 165);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x35FF08, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        m = game.add.sprite(130, 170, "mine_2");
        m.scale.setTo(0.5, 0.5);
	    m.inputEnabled = true;
        m.events.onInputDown.add(listenerClickM, this);
    }
    else{
        graphics = game.add.graphics(125, 165);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0xFF0808, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        m = game.add.sprite(130, 170, "mine_2");
        m.scale.setTo(0.5, 0.5);
        m.inputEnabled = true;
    }
    m.events.onInputOver.add(listenerM, this, 0, m.x, m.y);
	m.events.onInputOut.add(listenerOverTech);
    ///////////////////////// F
    if(researchF == 1){
        graphics = game.add.graphics(565, 165);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x334CFF, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        f = game.add.sprite(580, 180, "farms_2");
        f.scale.setTo(0.55, 0.8);
        f.inputEnabled = true;
    }
    else if(researchTH1 == 1 && researchF == 0 && lvlfarms >= 10){
        graphics = game.add.graphics(565, 165);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x35FF08, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        f = game.add.sprite(580, 180, "farms_2");
        f.scale.setTo(0.55, 0.8);
	    f.inputEnabled = true;
        f.events.onInputDown.add(listenerClickF, this);
    }
    else{
        graphics = game.add.graphics(565, 165);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0xFF0808, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        f = game.add.sprite(580, 180, "farms_2");
        f.scale.setTo(0.55, 0.8);
        f.inputEnabled = true;
    }
    f.events.onInputOver.add(listenerF, this, 0, f.x, f.y);
	f.events.onInputOut.add(listenerOverTech);
    //////////////////////// PP
    if(researchPP == 1){
        graphics = game.add.graphics(565, 500);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x334CFF, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        pp = game.add.sprite(570, 510, "energy_2");
        pp.scale.setTo(0.55, 0.55);
        pp.inputEnabled = true;
    }
    else if(researchTH2 == 1 && researchPP == 0 && lvlpowerPlant >= 10){
        graphics = game.add.graphics(565, 500);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x35FF08, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        pp = game.add.sprite(570, 510, "energy_2");
        pp.scale.setTo(0.55, 0.55);
	    pp.inputEnabled = true;
        pp.events.onInputDown.add(listenerClickPP, this);
    }
    else{
        graphics = game.add.graphics(565, 500);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0xFF0808, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        pp = game.add.sprite(580, 510, "energy_2");
        pp.scale.setTo(0.55, 0.55);
        pp.inputEnabled = true;
    }
    pp.events.onInputOver.add(listenerPP, this, 0, pp.x, pp.y);
	pp.events.onInputOut.add(listenerOverTech);
    //////////////////////// R
    if(researchR == 1){
        graphics = game.add.graphics(125, 500);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x334CFF, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        r = game.add.sprite(140, 520, "roads_2");
        r.scale.setTo(0.55, 0.55);
        r.inputEnabled = true;
    }
    else if(researchTH2 == 1 && researchR == 0 && lvlroads >= 10){
        graphics = game.add.graphics(125, 500);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x35FF08, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        r = game.add.sprite(140, 520, "roads_2");
        r.scale.setTo(0.55, 0.55);
	    r.inputEnabled = true;
        r.events.onInputDown.add(listenerClickR, this);
    }
    else{
        graphics = game.add.graphics(125, 500);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0xFF0808, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        r = game.add.sprite(140, 520, "roads_2");
        r.scale.setTo(0.55, 0.55);
        r.inputEnabled = true;
    }
    r.events.onInputOver.add(listenerR, this, 0, r.x, r.y);
	r.events.onInputOut.add(listenerOverTech);
    //////////////////////// H
    if(researchH == 1){
        graphics = game.add.graphics(345, 445);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x334CFF, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        h = game.add.sprite(350, 450, "housing_2");
        h.scale.setTo(0.30, 0.30);
        h.inputEnabled = true;
    }
    else if(researchTH2 == 1 && researchH == 0 && lvlhousing >= 10){
        graphics = game.add.graphics(345, 445);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x35FF08, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        h = game.add.sprite(350, 450, "housing_2");
        h.scale.setTo(0.30, 0.30);
	    h.inputEnabled = true;
        h.events.onInputDown.add(listenerClickH, this);
    }
    else{
        graphics = game.add.graphics(345, 445);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0xFF0808, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        h = game.add.sprite(350, 450, "housing_2");
        h.scale.setTo(0.30, 0.30);
        h.inputEnabled = true;
    }
    h.events.onInputOver.add(listenerH, this, 0, h.x, h.y);
	h.events.onInputOut.add(listenerOverTech);
    //////////////////////// B
    if(researchB == 1){
        graphics = game.add.graphics(345, 600);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x334CFF, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        b = game.add.sprite(350, 600, "barracks_2");
        b.scale.setTo(0.60, 0.60);
        b.inputEnabled = true;
    }
    else if(researchH == 1 && researchB == 0 && lvlbarracks >= 10){
        graphics = game.add.graphics(345, 595);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0x35FF08, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        b = game.add.sprite(350, 600, "barracks_2");
        b.scale.setTo(0.60, 0.60);
	    b.inputEnabled = true;
        b.events.onInputDown.add(listenerClickB, this);
    }
    else{
        graphics = game.add.graphics(345, 595);
        graphics.lineStyle(2, 0x0000FF, 1);
        graphics.beginFill(0xFF0808, 1.0);
        graphics.drawRect(0, 0, 140, 120);
        graphics.endFill();

        b = game.add.sprite(350, 600, "barracks_2");
        b.scale.setTo(0.60, 0.60);
        b.inputEnabled = true;
    }
    b.events.onInputOver.add(listenerB, this, 0, b.x, b.y);
	b.events.onInputOut.add(listenerOverTech);
}

function listenerClickBuilding() {
	
}

function update() {

}

function render() {

}
