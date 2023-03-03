import React, {useState} from "react";


function PostForm({OnAdd}) {
    const [name,setName]=useState('');
    const [color,setColor]=useState('');
    const [rom,setRom]=useState('');
    const [ram,setRam]=useState('');
    const [reload,setReload] = useState(false);
    const changeHandlerName =(e)=>{
       setName(e.target.value);
    }
    const changeHandlerColor =(e)=>{
        setColor(e.target.value);
     }
    const changeHandlerRom =(e)=>{
        setRom(e.target.value);
     }
    const changeHandlerRam =(e)=>{
        setRam(e.target.value);
     }
    
    const[isSubmited,setIsSubmited]=useState(false);
    const[error,setError]=useState(false);
    
  
    const submitHandler = (e) => {
        e.preventDefault();
        OnAdd({name,color,rom,ram,reload});
        setName('');
        setColor('');
        setRom('');
        setRam('');
    }

    return (
            <form method="post"  onSubmit={submitHandler}>
                <div className='text-field'>
                    <label for="name">Please Enter Name</label>
                    <input
                       type="text" id="name" placeholder="" 
                       onChange={(e)=>changeHandlerName(e)}
                        value={name}
                    />
                </div>
                <div className='text-field'>
                    <label for="color">Please Enter Color</label>
                    <input
                        type="text" id="color" placeholder="" 
                        onChange={(e)=>changeHandlerColor(e)}
                        value={color}
                    />
                </div>
                <div className='text-field'>
                    <label for="rom">Please Enter Rom</label>
                    <input
                        type="text" id="rom" placeholder="" 
                        onChange={(e)=>changeHandlerRom(e)}
                        value={rom}
                    />
                </div>
                <div className='text-field'>
                    <label for="ram">Please Enter Ram</label>
                    <input
                        type="text" id="ram" placeholder="" 
                        onChange={(e)=>changeHandlerRam(e)}
                        value={ram}
                    />
                </div>
                <div className='hero-btns'>
                    <button
                        className='btn btn-block'
                        buttonStyle='btn--primary'
                        buttonSize='btn--large'
                        type='submit'
                        
                    >
                        Submit<i className='far fa-play-circle' />
                    </button>
                </div>
                {isSubmited && <p> Form Submiter Successfully</p>}
                {error && <p> Error Occured</p>}
            </form>
            
        )
    
}

export default PostForm