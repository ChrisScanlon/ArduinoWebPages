<?php
header('Content-type: application/jsonp');
header('Access-Control-Allow-Origin: *');

/**
 * Represent a custom directory class call DirectoryLister where path is detailed
 */
class DirectoryLister implements JsonSerializable{
    
    private $path;

    /**
     * Instanciate a Directory with a path
     * @param string $path
     */
    function __construct(string $path){
        //check before if there are any files that exist
        if(file_exists($path)){
            $this->path = $path;
        }else{
            throw \Exception("Files do not exist for this path: $path");
        }
    }
    
    /**
     * Return filenames contained within the directory
     */
    function walk(){
        // scan directory and  
        foreach( scandir($this->path) as $basename){
            $new_path = $this->path.DIRECTORY_SEPARATOR.$basename ;
            // TODO: add a regex test
            if(!in_array($basename, ['.', '..']) && file_exists($new_path) ){
                yield $new_path;
            }
        }
    }
    
    /**
     * Convert this object into an array
     * @return array
     */
    function to_a(&$directories=null):array{
        if(!$directories){
            $directories = [];
        }
        
        foreach($this->walk() as $file){
            
            // if it's a directory, we loop on it
            if(is_dir($file)){
                $sub_dir = new DirectoryLister($file);
                $name = basename($file) ;
                $directories[$name] = [$name =>  $sub_dir->to_a($directories[$name]) ] ;
            // if it's a file
            }else{
                $name = basename($file) ;
                array_push($directories, $name);
            }  
        }
        return $directories;
        
    }
    
    /**
     * Overwritted function to specify json_encode() output
     * @return array
     */
    function jsonSerialize(){
        $array = $this->to_a();
        return $array;
    }
    
    function get_basename():string{return basename($this->path);}

    
}

$dir = new DirectoryLister('https://github.com/ChrisScanlon/ArduinoWebPages/');
$json =  json_encode($dir, JSON_PRETTY_PRINT);
echo $json ;
