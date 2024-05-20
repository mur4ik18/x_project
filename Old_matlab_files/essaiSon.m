function varargout = essaiSon(varargin)
% ESSAISON MATLAB code for essaiSon.fig
%      ESSAISON, by itself, creates a new ESSAISON or raises the existing
%      singleton*.
%
%      H = ESSAISON returns the handle to a new ESSAISON or the handle to
%      the existing singleton*.
%
%      ESSAISON('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in ESSAISON.M with the given input arguments.
%
%      ESSAISON('Property','Value',...) creates a new ESSAISON or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before essaiSon_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to essaiSon_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help essaiSon

% Last Modified by GUIDE v2.5 12-Dec-2018 23:01:37

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @essaiSon_OpeningFcn, ...
                   'gui_OutputFcn',  @essaiSon_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT

 
% --- Executes just before essaiSon is made visible.
function essaiSon_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to essaiSon (see VARARGIN)

% Choose default command line output for essaiSon
handles.output = hObject;
 handles.myMidiPlayer = Player()
 handles.ma = MesureAccord(accord_2018('Fa',2), Arpege(TonalPicks().notesToPick))
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes essaiSon wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = essaiSon_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes during object creation, after setting all properties.
function axes1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to axes1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called
plot([1 3 2])

% Hint: place code in OpeningFcn to populate axes1


% --- Executes on mouse press over axes background.
function axes1_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to axes1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
disp('CLIC ON PLOT')
 handles.ma.play(handles.myMidiPlayer);


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
disp('CALLBACK')
 handles.ma.play(handles.myMidiPlayer);

% --- If Enable == 'on', executes on mouse press in 5 pixel border.
% --- Otherwise, executes on mouse press in 5 pixel border or over pushbutton1.
function pushbutton1_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
disp('BUTTONDOWN')
 handles.ma.play(handles.myMidiPlayer);
