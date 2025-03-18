PROPIEDADES:
---------------------------
	padding: const EdgeInsets.only( right: 5),
	width: double.infinity,
	fit: BoxFit.cover,				//expande la imagen todo el ancho
	Navigator.pop(context);			//regresa a la anterior pantalla
	Platform.isAndroid				//si es android?
	final Map<String, dynamic> decodedData = json.decode(response.body);
	Color.fromRGBO(236,98,188,1)
BUENAS PRÁCTICAS:
---------------------------
	Text( name ?? 'No Title' )		//si es nulo
	children:[
		....
		if( name != null )			//condicion para mostrar
		  Container(
		  	....
		  )
		....
	]
	name!							//confiar en q no sera nulo
	BorderRadiusGeometry _borderRadius = BorderRadius.circular(10);
	final random= Random(); _width = random.nextInt(300).toDouble()+70;
	_color = Color.fromRGBO(random.nextInt(255),g,b,a);
	final Map<String, String> formValues = {
		'firs_name': 'Yhody',
		'last_name': 'ferte'
	}
	final List<int> imagesIds = [1,2,3,4,5];
		final lastId=imagesIds.last;
		imagesIds.addAll(
			[1,2,3,4,5].map((e)=>lastId+e)
		);
	final size = MediaQuery.of(context).size;		//logintud de pantalla

	PASAR PARAMETROS AL LLAMAR A OTRO SCREEN, MOVER A OTRA PANTALLA:
	------------------------------------------
		Navigator.pushNamed(context,'details',arguments:'movie-instance') // navegar a otra pantalla
		--EN EL OTRO SCREEN SE RECIBEN LOS PARAMETROS
			final String movie = ModalRoute.of(context)?.settings.arguments.toString() ?? 'no-movies';

			final Movie movie = ModalRoute.of(context)!.settings.arguments as Movie;


	parámetro opcional en funcion:
	funcion([int page=1])

	llamar a una propiedad dentro de un statefullwidget:
		widget.nombrefuncion();

	color html:
		color: Color(0xff30BAD6),

	Color iconos barra top:
		import 'package:flutter/services.dart';
		SystemChrome.setSystemUIOverlayStyle( SystemUiOverlayStyle.light);

CONTAINER:
-------------------------
	Container(
		width: double.infinity,
		height: 100,
		alignment: AlignmentDirectional.centerEnd,	//topCenter
		padding: EdgeInsets.only( right:20, top:20),
		color: Colors.red,
		decoration: BoxDecoration(
			color: Colors.red,
			borderRadius: BorderRadius.circular(20),
			gradient: LinearGradient(
				colors: [
						....
				]
			)
		),
		child:
	)
CONSTRAINEDBOX:
---------------------------
	ConstrainedBox(
		constraints: BoxConstraints( maxWidth: size.width - 190),
		child:[
			....
		]
	)
ALIGN:
----------------------------//en un Stack
	Align(
		alignment: Alignment.bottomCenter,
		child:
	)
CENTER:
----------------------------
	Center(
		child: Text('Details Screen',)
	)
TEXT:
-----------------------------
	Text(
		'Esto es un texto',
		maxLines:2,
		overflow: TextOverflow.ellipsis,
		textAlign:TextAlign.center,
		style: TextStyle(
			color: Colors.white
		)
	)
ANIMATEDCONTAINER:
--------------------------
	AnimatedContainer(
		duration: const Duration( milliseconds: 400),
		curve: Curves.bounceOut,
		.....
	)

SCAFFOLD:
--------------------------
	Scaffold(
		appBar: AppBar(
			title: const Text('Stan Lee'),
			actions: [
				Container(
					margin: const EdgeInsets.only( right:5),
					child: const CircleAvatar(
						child: Text('SL'),
						backgroundColor: Colors.indigo[900]
					)
				)
			]
		),
		body: _widget(),
		bottomNavigationBar: _widget(),
		floatingActionButton: FloatingActionButton(
					elevation:0,
					child: Icon(..),
					onPressed:(){}
				),
		floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked
	)
BOTTOMNAVIGATIONBAR:
---------------------------
	BottomNavigationBar(
		elevation:0,
		showSelectedLabels: false,
		showUnselectedLabels: false,
		selectedItemColor: Colors.pink,
		backgroundColor: Color.fromRGBO(55,57,84,1),
		unselectedItemColor: Color.fromRGBO(116,117,152,1),
		currentIndex:1,
		items: [
			BottomNavigationBarItem(
				icon: Icon( Icons.calendar_today_outlined, size:30),
				label: 'Calendario'
			),
			BottomNavigationBarItem(
				icon: Icon( Icons.calendar_today_outlined),
				label: 'Grafica'
			),
		],
		onTap: ( int i ) => ...function... que ejecuta
	)
TABLE:
--------------------------
	Table(
		children: [
			TableRow(
				children:[
					Text('Hola'),
					Text('Hola'),
				]
			),
			TableRow(
				children:[
					Text('Hola'),
					Text('Hola'),
				]
			)
		]
	)
STACK:
---------------------------
	Widgets unos emcima de otro
	Stack(
		alignment: Alignment.center,
		children:[
			Bckground(),
			Text('Hola Mundo')
		]
	)
SAFEAREA:
-----------------------------
	SafeArea(
		bottom:false,
		child:
	)
PAGEVIEW:
------------------------------
	PageView(
		physics: BouncingScrollPhysics(),
		scrollDirection: Axis.vertical,
		children: [
			Page1(),
			Page2()
		]
	)
ROW:
--------------------------
Row(
	mainAxisAlignment: MainAxisAlignment.end,
	children:[]
)
ICONBUTTON:
----------------------------
	IconButton(
		icon: Icon(Icons.search_outlined),
		onPressed: (){}
	)
GRADIENTES:
--------------------------
	En el scaffold no se puede agregar gradientes
	debe ser en un Container
	Normalmente se aplica en BOXDECORATION
	Container(
		decoration: BoxDecoration(
			gradient: LinearGradient(
				begin: Alignment.topCenter,
				end: Alignment.bottomCenter,
				stops: [0,0],
				colors:[
					Colors.red,
					Colors.green
				]
			)
		)
	)
BOXDECORATION:
--------------------------
	Container(
		decoration: BoxDecoration(
			gradient: LinearGradient(
				begin: Alignment.topCenter,
				end: Alignment.bottonCenter,
				stops: [0.2, 0.8],
				colors: [
					Color(0xff2E305F),
					Color(0xff202333)
				]
			)
		)
	)
TRANSFORM:
----------------------------
	ROTAR:
		Transform.rotate(
			angle: pi/12.0,
			child:
		)
POSITIONED:
	funciona dentro del stack
	Positioned(
		top: -100,
		left: -30,
		child:
	)
TEXTBUTTON:
---------------------------
TextButton(
	onPressed: (){},
	child: const Text('Cancel'),
	style: TextButton.styleFrom( 
		backgroundColor: Color(0xff0098FA),
		shape: StandiumBorder(),
		primary: Colors.indigo
	),
)

CIRCLEAVATAR:
--------------------------
	CircleAvatar(
		maxRadius: 110,
		backgroundImage: NetworkImage('https:........')
	)

ELEVATEDBUTTON:
---------------------------
ElevatedButton(
	style: ElevatedButton.styleFrom(
		primary: Colors.indigo,
		shape: const StadiumBorder(),
		elevation: 0
	),
	child: const Text('Mostrar alerta'),
	onPressed: (){

	}
)
SIZEBOX:
-------------------------
	SizeBox( height:10, child: ),

CARD:
--------------------------
Card(
	clipBehavior: Clip.antiAlias,					//corta todo lo q sobresalga
	shape: RoundedRectangleBorder(
		borderRadius: BorderRadius.circular(18)		//border del radius
	),
	elevation:10,
	shadowColor: AppTheme.primary.withOpacity(0.5),
	child: Column(
		children: [

		]
	)
)
IMAGE:
-------------------------
	Image(
		image: NetworkImage('https://....'),
	)
FADEINIMAGE:
--------------------------
	FadeInImage(
		image: NetworkImage('https://....'),
		placeholder: AssetImage('assets/jar-loading.gif'),
		width: double.infinity,
		height:230,
		fit: BoxFit.cover,			//adaptar al contenedor padre
		fadeInDuration: Duration(milliseconds: 300),
	)
CLIPRRECT:
-------------------------
	ClipRRect(
		borderRadius: BordeRadius.circular(20),
		child;
	)
BACKDROPFILTER:
	BackdropFilter(
		filter: ImageFilter.blur( sigmaX: 5, sigmaY: 5),
		child:
	)
GESTUREDETECTOR:
-------------------------
	GestureDetector(
		onTap: () => Navigator.pushNamed(context,'details',arguments:'movie-instance'),
		child: 
	)
LISTTILE
---------------------------
	ListTile(
		leading: Icon( Icons.access_time_sharp, color: AppTheme.primary ),
		title: Text('Hola mundo'),
		subtitle: Text('Subtitulo'),
		trailing: Icon( Icons.keyboard_arrow_right,color: Colors.grey),
		onTap: () => print('abrir algo...'),
	)
DISMISSIBLE:  		//Va dentro de ListView.builder
---------------------------
	itemBuilder: ( _,i )=> Dismissible(
		key: UniqueKey(),
		background: Container(
			color: Colors.red,
		),
		onDismissed: (DismissDirection direction){
			Provider.of(<ScanListProvider>(context, listen: false).primaryColor),
		},
		child: ListTile(...)
	)
LISTVIEW:
---------------------------

ListView(
	padding: const EdgeInsets.symmetric( horizontal:20, vertical:10),
	children: const[
		ListTile(
			leading: Icon( Icons.access_time_sharp ),
			title: Text('Hola mundo'),
		)
	]
) ListTile

final options = const['Megaman', 'Metal Gear', 'Super man'];
ListView(
	children: const[
		...options.map(
			(e) => ListTile(
				title: Text( game ),
				trailing: const Icon( Icons.arrow_forward_ios_outlined ),
			)
		).toList()
	]
) ListTile
----------------------------------------------------------
final options = const['Megaman', 'Metal Gear', 'Super man'];
ListView.builder(			//el tamaño del padre debe ser fijo
	scrollDirection: Axis.horizontal,
	itemCount: options.length,
	itemBuilder: (context,i) => ListTile(
		title: Text( options[i]),
		trailing: const Icon( Icons.arrow_forward_ios_outlined ),
	),
	separatorBuilder: ( _ , __) => const Divider(),
)
---------------------
	final ScrollController scrollController = ScrollController();

	@override
	void initState(){
		super.initState();
		scrollController.addListener((){
			print('${scrollController.position.pixels}, ${scrollController.position.maxScrollExtent}');
		});
	}

	body: MediaQuery.removePadding(				//sirver para ocultar el espacio top del appbar
		context: context,
		removeTop: true,
		removeBottom true,
		child: ListView.builder(
			physics: const BouncingScrollPhysics(),
			controller: scrollController,
			itemCount: 10,
			itemBuilder: (BuildContext context, int index){
				return FadeInImage(
					width: double.infinity,
					height: 300,
					fit: BoxFit.cover,
					placeholder: const AssetImage('assets/jar-loading.gif'),
					image: NetworkImage('https://....')
				)
			}
		)
	)


NAVEGAR A OTRA PANTALLA (MANUALMENTE)
--------------------------------------------------
ListView.separated(
	itemBuilder: (context, index) => ListTile(
		leading: const Icon( Icons.access_tine_outlined),
		title: const Text('Nombre de ruta'),
		onTap: () {
			final route = MaterialPageRoute(
				builder: (context) => const Listview1Screen(),	//widget a donde se navega
			);
			Navigator.push(context, route); 					//navega a la ruta
		}
	),
	separatorBuilder: ( _, __ ) => const Divider(),
	itemCount: 100												//cantidad a mostrar
)
NAVEGAR A OTRA PANTALLA (CON RUTA)
--------------------------------------------------
ListView.separated(
	itemBuilder: (context, index) => ListTile(
		leading: const Icon( Icons.access_tine_outlined),
		title: const Text('Nombre de ruta'),
		onTap: () {
			Navigator.pushNamed(context, 'card');				//se llama al nombre de la ruta
		}
	),
	separatorBuilder: ( _, __ ) => const Divider(),
	itemCount: 100												//cantidad a mostrar
)

CONFIGURAR RUTAS
---------------------------------------------
return MaterialApp(
	debugShowCheckedModeBanner: false,
	title: 'Material App',
	initialRoute: 'home',
	routes: {
		'home'		: (BuilderContext context) => const HomeScreen(),
		'listview1'	: (BuilderContext context) => const Listview1Screen(),
		'alert'	: (BuilderContext context) => const AlertScreen(),
		'card'	: (BuilderContext context) => const CardScreen(),
		'mapa' 	:  ( _ ) => MapaPage()
	},
	onGenerateRoute: (settings){
		return MaterialPageRoute(
			builder: (context) => const AlertScreen(),						//sirve para rutas dinámicas en caso no exista el nombre de la ruta
		);
	}
)

TEMAS:
----------------
retur MaterialApp(
	debugShowCheckedModeBanner: false,
	title: 'Material App',
	...
	theme: ThemeData.light().copyWith(			//ó ThemeData(
		primaryColor: Colors.indigo,			//Color primario
		appBarTheme: const AppBarTheme(				//AppBarTheme
			color: Colors.red,
			elevation: 0
		),
		floatingActionButtonTheme: FloatingActionButtomThemeData(
			backgroundColor: Colors.deepPurple
		),
		scaffoldBackgroundColor: Colors.black
	),
)

COLUMN
-------------------------
Column(
	mainAxisSize: MainAxisSize.min,				//los hijos determinan su tamaño,
	crossAxisAlignment: CrossAxisAlignment.start,
)

FLUTTERLOGO
---------------
	FlutterLogo( size:100)	//flutter de logo



SHOWDIALOG y ALERTDIALOG
--------------------------

showDialog(
	barrierDismissible: true,					//se cierra cuando se presiona en el fondo
	context: context,
	builder: (context){
		return AlertDialog(
			elevation: 5,
			title: const Text('Titulo'),
			shape: RoundedRectangleBorder( borderRadius: BorderRadiusDirectional.circular(100)),
			content: Column(
				children: const [
					Text('Este es el contenido de la alerta')
				],
			),
			actions:[
				TextButton(
					onPressed: (){

					}, 
					child: const Text('Cancelar')
				)
			],
		);
	}
)
SHOWCUPERTINODIALOG
--------------------------------

showCupertinoDialog(
	barrierDismissible: true,
	context: context, 
	builder: ( context ){
		return CupertinoAlertDialog(
			title: const Text('Titulo'),
			content: Column(
				mainAxisSize: MainAxisSize.min,
				children: const [
					Text('este es el contenido de la alerta'),
					SizeBox( height:10 ),
					FlutterLogo( size: 100 )
				],
			),
			actions:[
				TextButton(
					onPressed: () => Navigator.pop(context),
					child: const Text('Cancelar' style: TextStyle( color: Colors.red ))
				)
			],
		)
	}
)
TEXTSTYLE
-----------------------
	TextStyle( 
		color: Colors.red 
		fontSize: 20,
		fontWeight:FontWeight.bold,
	)
CIRCULARPROGRESSINDICATOR
-------------------------
	Un ícono para cargar
		CircularProgressIndicator(),
	Funciona igual para
		CupertinoActivityIndicator(),

SINGLECHILDSCROLLVIEW
----------------------------
	SingleChildScrollView(
		child:
	)
SLIVERS:
---------------------------
---------------------------
	CUSTOMSCROLLVIEW			//actua como SingleChildScrollView
	----------------
		CustomScrollView(
			slivers:[

			]
		)
	SLIVERAPPBAR
	------------
		SliverAppBar(
			backgroundColor: Colors.indigo,
			expandedHeight: 200,
			floating: false,
			pinned: true,
			flexibleSpace: FlexibleSpaceBar(
				centerTitle: true,
				titlePadding: EdgeInsets.add(0),
				title: Container(
					width: double.infinity,
					alignment: Alignment.bottomCenter,
					color: Colors.black12,
					child: Text(
						'movie.title',
						style: TextStyle( fontSize: 16 ),
					)
				),
				background: FadeInImage(
					placeholder: AssetImage('assets/image.png'),
					image: NetworkImage('https://via.placeholder.com/500x300'),
					fit: BoxFit.cover,
				)
			)
		)
	SLIVERLIST
	----------
		SliverList(
			delegate: SliverChildListDelegate([
				...
			])
		)
SLIDER:
---------------------
	Slider(			//Slider.adaptive(.......
		min:50,
		max: 400,
		value: 100,
		activeColor: AppTheme.primary,
		divisions: 10,
		onChanged: (value){

		}
	),
	Image(
		image: NetworkImage('https://....'),
		fit: BoxFit.contain,					//corta la imagen 
		width: _sliderValue,					//valor cambiando
	)
EXPANDED:
----------------------------
	Expanded(				//que tome todo el ancho posible todo ese widget
		child: SingleChildScrollView(
			child: Image(
				image: const NetworkImage('https://....'),
				fit: BoxFit.contain,
				width: _SliderValue,
			)
		)
	)
POSITIONED:
-------------------------------
	Positioned(
		bottom: 40,
		left: size.width * 0.5 - 30,
		child: 
	)
STACK:					//Colocar widgets ensima de otros
-------------------------
	Stack(
		children:[
		]
	)
REFRESHINDICATOR(
	color: AppTheme.primary,
	onRefresh:onRefresh,
	child:
)
IMAGE:
-----------------------------
	Image.asset('assets/img/background1.jpg',
				width: MediaQuery.of(context).size.width,
				height: MediaQuery.of(context).size.height,
				fit: BoxFit.cover,
				color: Colors.black4554,
				colorBlendMode:BlendMode.darken
			),
FUTUREBUILDER:
--------------
	espera que algo se termine o se reciba. Este algo puede ser algo como una petición a internet, cargar una imagen, o simplemente algo que tomará tiempo, como calcular un número
	Mostrar cosas mientras esperas
	Actualizar cuando llegue
	return FutureBuilder(
		future: Future,
		initialData: InitialData,
		builder: (BuildContext context, AsyncSnapshot<List<Cast>> snapshot){
			if(!snapshot.hasData){
				return Container(
					constraints: BoxContraints(maxWidth: 150),
					height: 180,
					child: CupertinoActivityIndicator(),
				)
			}
			final List<Cast> cast = snapshot.data!;
			return Container(
				margin: EdgeInsets.only( bottom: 30 ),
				width: double.infinity,
				height: 180,
				child: ListView.builder(
					itemCount: 10,
					scrollDirection: Axis.horizontal,
					itemBuilder: ( _, int index) => _CastCard(cast[index]),
				),
			);
		},
	),
FUTURE:
-------------------------------
	Future<void> onRefresh() async{
		await Future.delayed( const Duration( seconds: 2 ));
		final lastId = imagesIds.last;
		imagesIds.clear();
		imagesIds.add(lastId+1);
		add5();
	}

	Future<List<Cast>> getMovieCast( int movieId ) async {
		if( movieCast.containsKey(movieId)) return moviesCast[movieInd]!;

		print('pidiendo info al servidor .cast');

		...

		moviesCast[movieId] = creditsResponse.cast;
		return creditsResponse.cast;
	}
SHOWSEARCH
-----------------------------------
	Tiene un asistente que ayuda a buscar
	AppBar(
		title: Text('Peliculas en cines'),
		elevation: 0,
		actions: [
			IconButton(
				icon: Icon( Icons.search_outlined ),
				onPressed: () => showSearch(context: context, delegate:MovieSearchDelegate()),
			)
		]
	)
	class MovieSearchDelegate extends SearchDelegate{
		@override
		String get searchFieldLabel => 'Buscar película';

		@override
		Widget buildSuggestions(BuildContext context){
			return Text('buildSuggestions: $query');
		}

	}
FORMULARIOS:
----------------------------
	TextFormField(					//tienen mas interacciones en un formulario
		autofocus: true,
		initialValue: 'Yhody',
		textCapitalization: TextCapitalization.words,
		keyboardType: TextInputType.emailAddress,
		obscureText: true,
		onChanged:(value){

		},
		validator:(value){
			if(value==null) return 'Este campo es requerido';
			return value.length < 3 ? 'mínimo de 3 letras' : null;
		},
		autovalidateMode: AutoValidateMode.onUserInteraction,
		decoration: InputDecoration(
			hintText: 'Nombre de usuario',
			labelText: 'Nombre',
			helperText: 'Sólo letras',
			counterText: '3 caracteres',
			prefixIcon: Icon( Icons.group_outlined),
			suffixIcon: Icon( Icons.group_outlined),
			icon: Icon( Icons.group_outlined),
			border: OutlineInputBorder(
				borderRadius: BorderRadius.only(
					bottomLeft: Radius.circular(10),
					topRight: Radius.circular(10),
				)
			)
		)
	)
	TextField:
	-------------------
	TextField(						// no se usa en formularios
		decoration: InputDecoration(
			label: Text('Correo Electrónico'),
			prefixIcon: Icon(
				Icons.email,
				color: Colors.white,
			),
			enabledBorder: UnderlineInputBorder(
				borderSide:BorderSide(color: Colors.white)
			),
			focusedBorder: UnderlineInputBorder(
				borderSide: BorderSide(color: Colors.white)
			)
		)
	)

	final GlobalKey<FormState> myFormKey = GlobalKey<FormState>();
	Form(
		key: myFormKey,
		child: Column(
			children:[
				...cajas de texto.....
				ElevatedButton(
					child: const SizedBox(
						width: double.infinity,
						child: Center(child: const Text('guardar'))
					),
					onPressed:(){
						FocusScope.of(context).requestFocus(FocusNode());		//oculta el teclado
						if(!myFormKey.currentState!.validate()){
							return;
						}
					}
				)
			]
		)
	)
	DropdownButtonFormField<String>(
		value: 'Admin',
		items:[
			DropdownMenuItem( value:'Admin', child: Text('Admin')),
		],
		onChanged: (value){

		}
	)
	Checkbox(
		value: _sliderEnabled,
		onChanged: (value ){
			_sliderEnabled = value??true;
			setState(){};
		}
	)
	CheckboxListTile(
		activeColor: AppTheme.primary,
		title: const Text('Habulitar Slider'),
		value: _sliderEnabled,
		onChanged: (value ){
			_sliderEnabled = value??true;
			setState(){};
		}
	)
	Switch(
		value: _sliderEnabled,
		onChanged: (value ){
			_sliderEnabled = value;
			setState(){};
		}
	)
	SwitchListTile(						//SwitchListTile.adaptive
		activeColor: AppTheme.primary,
		title: const Text('Habulitar Slider'),
		value: _sliderEnabled,
		onChanged: (value ){
			_sliderEnabled = value??true;
			setState(){};
		}
	)

	const AboutListTile(),				//muestra todas las licencias que el app usa

ANIMACIONES:
-----------------------------------------------
Curvas: https://api.flutter.dev/flutter/animation/Curves-class.html


WIDGETS DE TERCEROS:
----------------------------
----------------------------
SWIPER			:https://pub.dev/packages/card_swiper
-----------------------
	Swiper(
		itemCount: 10,
		layout: SwiperLayout.STACK,
		itemWidth: size.width * 0.6,
		itemHeight: size:height * 0.9,
		itemBuilder: ( _, int index){

		}
	)


PROVIDER
----------------------
	Código del provider:
		class ToyStore extends ChangeNotifier {
		  int _toyCount = 0;

		  int get toyCount => _toyCount;

		  void addToy() {
		    _toyCount++; // Agregar un juguete.
		    notifyListeners(); // Avisar a todos que el número cambió.
		  }
		}
	Código para compartir datos:
		import 'package:flutter/material.dart';
		import 'package:provider/provider.dart';
		import 'toy_store.dart'; // Aquí está la tienda.

		void main() {
		  runApp(
		    ChangeNotifierProvider(
		      create: (context) => ToyStore(),
		      child: MyApp(),
		    ),
		  );
		}

		class MyApp extends StatelessWidget {
		  @override
		  Widget build(BuildContext context) {
		    return MaterialApp(
		      home: ToyCounterScreen(),
		    );
		  }
		}

		class ToyCounterScreen extends StatelessWidget {
		  @override
		  Widget build(BuildContext context) {
		    // Obtenemos el número de juguetes desde el provider.
		    int toyCount = context.watch<ToyStore>().toyCount;

		    return Scaffold(
		      appBar: AppBar(title: Text("Juguetes")),
		      body: Center(
		        child: Column(
		          mainAxisAlignment: MainAxisAlignment.center,
		          children: [
		            Text("Tenemos $toyCount juguetes"),
		            SizedBox(height: 20),
		            ElevatedButton(
		              onPressed: () {
		                // Llamamos a addToy() para agregar un juguete.
		                context.read<ToyStore>().addToy();
		              },
		              child: Text("Agregar juguete"),
		            ),
		          ],
		        ),
		      ),
		    );
		  }
		}

MULTIPROVIDER
-------------
	Creamos los providers:
		class ToyStore extends ChangeNotifier {
		  int _toyCount = 0;

		  int get toyCount => _toyCount;

		  void addToy() {
		    _toyCount++;
		    notifyListeners(); // Notifica a los widgets que usan este provider.
		  }
		}

		class BookStore extends ChangeNotifier {
		  int _bookCount = 0;

		  int get bookCount => _bookCount;

		  void addBook() {
		    _bookCount++;
		    notifyListeners();
		  }
		}
	Configuramos el MultiProvider:
		void main() {
		  runApp(
		    MultiProvider(
		      providers: [
		        ChangeNotifierProvider(create: (context) => ToyStore(), lazy: false), // lazy: false, carga al inicio del widget
		        ChangeNotifierProvider(create: (context) => BookStore()),
		      ],
		      child: MyApp(),
		    ),
		  );
		}
	Usamos los datos en los widgets:
		class MyApp extends StatelessWidget {
		  @override
		  Widget build(BuildContext context) {
		    return MaterialApp(
		      home: DashboardScreen(),
		    );
		  }
		}

		class DashboardScreen extends StatelessWidget {
		  @override
		  Widget build(BuildContext context) {
		    int toyCount = context.watch<ToyStore>().toyCount;
		    int bookCount = context.watch<BookStore>().bookCount;

		    //int bookCount= Provider.of<BookStore>(context,listen:false); //es igual q el anterior pero no escucha los cambios o no actualiza el widget

		    return Scaffold(
		      appBar: AppBar(title: Text("Tienda Infantil")),
		      body: Center(
		        child: Column(
		          mainAxisAlignment: MainAxisAlignment.center,
		          children: [
		            Text("Juguetes: $toyCount"),
		            Text("Libros: $bookCount"),
		            SizedBox(height: 20),
		            ElevatedButton(
		              onPressed: () => context.read<ToyStore>().addToy(),
		              child: Text("Agregar juguete"),
		            ),
		            ElevatedButton(
		              onPressed: () => context.read<BookStore>().addBook(),
		              child: Text("Agregar libro"),
		            ),
		          ],
		        ),
		      ),
		    );
		  }
		}

CONVERTIR JSON A CLASE RESPONSE
-------------------------------
	URL: https://app.quicktype.io/

CONTROLADORES:
-------------------------------
	los controladores son una herramienta muy útil para manejar y gestionar el estado de los widgets que interactúan con el usuario, el desplazamiento, las animaciones y otros comportamientos dinámicos de la UI.
	@override
	void initState(){
		super.initState();
		scrollController.addListener((){
			print( scrollController.position.pixels );
			print( scrollController.position.maxScrollExtent );

			if( scrollController.position.pixels >= scrollController.position.maxScrollExtent - 500){
				print('Obtener siguiente página');

			}
		});
	}
	@override
	void dispose(){


		super.dispose();
	}


PLUGIMS:
----------------------

	sqflite:
		https://pub.dev/packages/sqflite#-readme-tab-
	path_provider
		https://pub.dev/packages/path_provider#-installing-tab-


SPASH SCREEN
----------------------
	importar: flutter_native_splash: ^2.3.3
	crear archivo flutter_native_splash.yaml en la raiz
	ejecutar: flutter pub run flutter_native_splash:create

CONFIGURACIONES ANDROID
----------------------------
	Gradle 8.1 y JAVA 21
	archivo settings.gradle
	plugins {
	    id "dev.flutter.flutter-plugin-loader" version "1.0.0"
	    id "com.android.application" version "8.2.1" apply false
	    id "org.jetbrains.kotlin.android" version "1.9.10" apply false
	}

PREFERENCIAS:
---------------------------
	prefer_const_constructors 
	----------------------------
	Esta regla está diseñada para alentar a los desarrolladores a usar constructores constantes (const) siempre que sea posible
	en analysis_options.yaml dentro de linter

BLOC:
-------------------
	flutter_bloc: ^8.1.6

	
	studios jhon jhonson ayuno intermitente
	
	admin
	#4AFCD0@E97762*



	6n.2Ki@DJ6Uv*Zz
 	

 	ALTER TABLE `formatos` ADD `configuracion` VARCHAR(100) NULL AFTER `item`;
 	ALTER TABLE `formatos_empresa` ADD `configuracion` VARCHAR(100) NULL AFTER `item`;
 	UPDATE `formatos` SET `configuracion` = '{\"height_min\":210,\"height_item\":10}' WHERE `formatos`.`id` = 10;



 	 


